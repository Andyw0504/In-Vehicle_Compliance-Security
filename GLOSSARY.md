# 术语表（Glossary）

> 中英对照速查。按主题分组，按字母序。

## 组织与法规

| 术语 | 全称 | 含义 |
|---|---|---|
| CSMS | Cyber Security Management System | 网络安全管理体系（R155 组织层认证对象） |
| SUMS | Software Update Management System | 软件升级管理体系（R156） |
| WP.29 | World Forum for Harmonization of Vehicle Regulations | 联合国车辆法规协调论坛 |
| VTA | Vehicle Type Approval | 车辆型式认证（准入） |
| FedR | Function to discover Relevance | R155 要求的漏洞相关性发现机制 |
| PSIRT | Product Security Incident Response Team | 产品安全事件响应团队 |
| TARA | Threat Analysis and Risk Assessment | 威胁分析与风险评估（21434 核心） |
| SOTIF | Safety Of The Intended Functionality | 预期功能安全（ISO 21448） |

## 标准

| 术语 | 含义 |
|---|---|
| UN R155 | 网络安全与 CSMS 法规（准入强制） |
| UN R156 | 软件升级与 SUMS 法规 |
| ISO/SAE 21434 | 道路车辆网络安全工程标准 |
| ISO 24089 | 软件更新工程标准 |
| ISO 14229 (UDS) | 统一诊断服务 |
| ISO 13400 (DoIP) | 基于以太网的诊断 |
| ISO 15765-2 (DoCAN) | CAN 上的诊断传输层 |
| GB 44495-2024 | 汽车整车信息安全技术要求（中国强标，2026.1.1 实施） |
| GB 44496-2024 | 汽车软件升级通用技术要求（中国强标） |

## 总线与网络

| 术语 | 含义 |
|---|---|
| CAN / CAN-FD | 控制器局域网 / 可变数据速率升级版（64B 数据段） |
| LIN | 低成本本地互联网络（主从） |
| FlexRay | 时间触发高带宽总线 |
| 100/1000BASE-T1 | 车载以太网（单对双绞线） |
| ECU | Electronic Control Unit 电子控制单元 |
| Gateway | 网关，域间报文路由与过滤 |
| Domain / Zonal | 域集中架构 / 区域控制器架构 |
| DBC | CAN 报文数据库定义文件（信号解析） |
| DLC | Data Length Code 数据长度码 |
| BUS OFF | 错误计数超限后节点离线状态 |

## 车载部件

| 术语 | 含义 |
|---|---|
| TBOX / TCU | Telematics Box/Unit 远程通信终端（蜂窝入口） |
| IVI | In-Vehicle Infotainment 车载信息娱乐（车机） |
| BCM | Body Control Module 车身控制模块 |
| EPS / ESP | 电动助力转向 / 车身电子稳定系统 |
| RKE | Remote Keyless Entry 遥控钥匙 |
| PEPS | Passive Entry Passive Start 无钥匙进入启动 |
| OBD-II | 车载诊断接口（16 针，诊断入口） |
| V2X | Vehicle-to-Everything 车联网通信 |

## 安全机制

| 术语 | 含义 |
|---|---|
| secOC | AUTOSAR Secure Onboard Communication（MAC+新鲜度） |
| HSM | Hardware Security Module 硬件安全模块（EVITA Full/Medium/Light） |
| SHE | Secure Hardware Extension 安全硬件扩展（HSM 前身简化版） |
| Secure Boot | 安全启动（信任链逐级验签） |
| IDS | Intrusion Detection System 入侵检测 |
| OTA | Over-The-Air 空中升级 |
| Uptane | 车用安全 OTA 框架（双仓库签名） |
| Seed-Key | 0x27 安全访问的挑战-响应机制 |
| DID | Data Identifier（0x22 读 / 0x2E 写的数据标识） |
| DTC | Diagnostic Trouble Code 诊断故障码 |
| NRC | Negative Response Code 否定响应码 |
| Attack Surface | 攻击面：所有可触达的接口与信道 |
| Cybersecurity Claim | 网络安全声明：缓解措施可验证的陈述（21434） |
