#!/usr/bin/env bash
# CAN 实验环境一键搭建: vcan0 虚拟总线 + 工具检查
# 用法: sudo ./vcan_setup.sh
set -e

[ "$(id -u)" -eq 0 ] || { echo "请用 sudo 运行"; exit 1; }

echo "[1/4] 加载 vcan 内核模块"
modprobe vcan 2>/dev/null || { echo "  模块加载失败, 检查内核: uname -r"; exit 1; }

echo "[2/4] 创建虚拟总线 vcan0"
ip link show vcan0 >/dev/null 2>&1 || ip link add dev vcan0 type vcan
ip link set up vcan0
ip -brief link show vcan0

echo "[3/4] 检查工具链"
for t in candump cansend cansniffer canplayer; do
    command -v $t >/dev/null && echo "  ✓ $t" || echo "  ✗ $t 缺失 → apt install can-utils"
done
python3 -c "import can" 2>/dev/null && echo "  ✓ python-can" || echo "  ✗ python-can 缺失 → pip3 install python-can"

echo "[4/4] 冒烟测试"
cansend vcan0 123#DEADBEEF && timeout 2 candump -n 1 vcan0 && \
    echo "✓ 环境就绪! 试试: cansend vcan0 188#0102 && cansniffer -c vcan0"
