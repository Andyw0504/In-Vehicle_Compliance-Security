# 🚗 In-Vehicle Compliance & Security

> 车辆网络安全双轨学习仓库：**法规合规** 与 **技术安全** 同步推进，持续记录学习笔记与进度。

## 🗺️ 两条路线

| 路线 | 目标 | 入口 |
|---|---|---|
| **A · 法规合规** | 读懂 UN R155/R156、ISO/SAE 21434 体系，掌握国内 GB 强标与数据合规要求 | [docs/compliance/](docs/compliance/) |
| **B · 技术安全** | 掌握车辆网络架构、CAN 总线、UDS 诊断协议，能做总线分析与安全测试 | [docs/technical/](docs/technical/) |

- 📅 总体节奏：[PLAN.md](PLAN.md)（16 周双轨计划）
- 📝 每周复盘：[WEEKLY.md](WEEKLY.md)

## 路线 A · 法规合规

| # | 手册 | 状态 |
|---|---|---|
| 01 | [监管框架总览](docs/compliance/01-监管框架总览.md)（WP.29 / R155 / R156 / 21434 / 国内体系） | 🔄 |
| 02 | [UN R155 与 CSMS 网络安全管理体系](docs/compliance/02-UN-R155与CSMS.md) | ⬜ |
| 03 | [ISO/SAE 21434 网络安全工程精读](docs/compliance/03-ISO-21434网络安全工程.md)（TARA 方法论） | ⬜ |
| 04 | [国内法规与数据合规](docs/compliance/04-国内法规与数据合规.md)（GB 44495/44496、汽车数据规定） | ⬜ |
| 05 | [合规落地与实践](docs/compliance/05-合规落地实践.md)（认证流程、体系文件、审计应对） | ⬜ |

## 路线 B · 技术安全

| # | 手册 | 状态 |
|---|---|---|
| 01 | [汽车电子与总线架构基础](docs/technical/01-汽车电子与总线架构.md) | ⬜ |
| 02 | [CAN 总线安全实操](docs/technical/02-CAN总线安全实操.md)（SocketCAN / can-utils / 靶场） | ⬜ |
| 03 | [诊断协议与 UDS](docs/technical/03-诊断协议与UDS.md)（ISO 14229 / 0x27 安全访问 / DoIP） | ⬜ |
| 04 | [攻击面与经典案例](docs/technical/04-攻击面与经典案例.md)（TCU / IVI / RKE / OTA） | ⬜ |
| 05 | [车端防御体系](docs/technical/05-车端防御体系.md)（secOC / HSM / IDS / 安全启动） | ⬜ |

## 📚 资源

- [学习资源汇总](docs/resources/学习资源汇总.md)：标准原文获取、书籍、课程、工具、社区

---

> ⚠️ 车辆安全研究必须**只在自有测试环境 / 台架 / 试验场**进行，严禁对真实在用车辆实施未授权测试。
