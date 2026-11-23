#!/usr/bin/env python3
"""CAN 信号定位助手: 从 candump 日志中找出"会变化的字节"
用法:
    1) candump -L vcan0 > capture.log     # 采集期间操作车辆/模拟器(踩油门/开门锁)
    2) python3 can_signal_finder.py capture.log

原理: 按 ID 分组, 逐字节统计取值范围; 变化字节 = 潜在信号,
      连续多字节单调变化 = 疑似 16bit 数值型信号(如车速)。
"""
import sys
import re
from collections import defaultdict

LINE_L = re.compile(r'\(([\d.]+)\)\s+\S+\s+([0-9A-Fa-f]+)#([0-9A-Fa-f]*)')
LINE_S = re.compile(r'^\s*\S+\s+([0-9A-Fa-f]+)\s+\[\d+\]\s+(.*)$')


def parse(path):
    frames = []  # (id, data_tuple)
    for line in open(path, errors='ignore'):
        m = LINE_L.search(line)
        if m:
            fid = int(m.group(2), 16)
            data = bytes.fromhex(m.group(3))
            frames.append((fid, data))
            continue
        m = LINE_S.match(line)
        if m:
            fid = int(m.group(1), 16)
            data = bytes.fromhex(m.group(2).replace(' ', ''))
            frames.append((fid, data))
    return frames


def main(path):
    frames = parse(path)
    if not frames:
        sys.exit('未解析到报文, 确认用 candump -L 或标准格式保存')
    per_id = defaultdict(list)
    for fid, data in frames:
        per_id[fid].append(data)

    print(f'共 {len(frames)} 帧, {len(per_id)} 个 ID\n')
    print(f'{"ID":<8}{"帧数":<8}疑似信号字节(下标: 最小~最大)')
    for fid, datas in sorted(per_id.items()):
        width = max(len(d) for d in datas)
        ranges = [None] * width
        for d in datas:
            for i, b in enumerate(d):
                lo, hi, cnt = ranges[i] or (255, 0, 0)
                ranges[i] = (min(lo, b), max(hi, b), cnt + 1)
        changing = [f'{i}:{lo:#04x}~{hi:#04x}' for i, (lo, hi, _) in enumerate(ranges) if lo != hi]
        if changing:
            print(f'{fid:#06x}  {len(datas):<8}{", ".join(changing)}')
        # 相邻两字节都变化 → 提示可能是 16bit 信号
        hot = [i for i, (lo, hi, _) in enumerate(ranges) if lo != hi]
        pairs = [i for i in hot if i + 1 in hot and i % 2 == 0]
        if pairs:
            print(f'         ↳ 字节 {pairs} 相邻变化, 疑似 16bit 数值信号(车速/转速类)')
    print('\n下一步: cansniffer -c 边操作边验证; DBC 还原可用 cantools 库')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
