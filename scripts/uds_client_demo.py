#!/usr/bin/env python3
"""UDS 客户端演示(ISO-TP 单帧版): 诊断会话 / 读DID / 0x27 安全访问流程
依赖: pip3 install python-can
用途: 在 vcan0 + 开源 UDS Server(如 UDSim) 或自有 ECU 台架上练习。
      完整多帧/流控请用 python-isotp + udsoncan 库, 本脚本演示原理。
"""
import can

bus = can.interface.Bus(channel='vcan0', bustype='socketcan')


def send_uds(data, timeout=1.0):
    """单帧发送 + 等待响应(忽略 ISO-TP 流控帧)"""
    assert len(data) <= 7, '单帧最多 7 字节负载, 超长请用 python-isotp'
    sf = can.Message(arbitration_id=0x7E0, data=bytes([len(data)]) + bytes(data),
                     is_extended_id=False)
    bus.send(sf)
    while True:
        resp = bus.recv(timeout)
        if resp is None:
            raise TimeoutError('UDS 响应超时')
        if resp.arbitration_id in (0x7E8,) and resp.data[0] >> 4 != 0x3:  # 跳过流控
            payload = resp.data[1:1 + (resp.data[0] & 0x0F)]
            return payload


def negative_hex(payload):
    """0x7F SID NRC → 返回否定响应码"""
    return f'否定响应 SID={payload[1]:#04x} NRC={payload[2]:#04x}'


print('== 1. 进入扩展会话 (10 03) ==')
r = send_uds([0x10, 0x03])
print(' →', r.hex() if r[0] != 0x7F else negative_hex(r))

print('== 2. 读 DID (22 F1 90, VIN 示例) ==')
r = send_uds([0x22, 0xF1, 0x90])
print(' →', r.hex() if r[0] != 0x7F else negative_hex(r))

print('== 3. 安全访问 (27 01 → seed; 本地算 key; 27 02 发 key) ==')
r = send_uds([0x27, 0x01])
if r[0] == 0x67:
    seed = r[2:]
    print(f' → seed = {seed.hex()}')
    key = seed_key_algorithm(seed)  # ← 换成目标 ECU 的算法(通常需固件逆向)
    r = send_uds([0x27, 0x02] + list(key))
    print(' → 解锁成功' if r[0] == 0x67 else ' → ' + negative_hex(r))
else:
    print(' → ' + negative_hex(r))


def seed_key_algorithm(seed: bytes) -> bytes:
    """示例占位算法: key = ~seed (真实算法藏在固件里, 需逆向获取)"""
    return bytes(~b & 0xFF for b in seed)
