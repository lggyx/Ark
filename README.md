 <div align="center">

# ⬡ ARK · 文明守望

**`Offline Knowledge Survival Node`**  
**`离线知识生存节点 · 数字文明火种`**

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Building-orange.svg)]()
[![Platform](https://img.shields.io/badge/Platform-OnePlus_8T-55efc4.svg)]()

*当最后一根网线断裂，*  
*当最后一座基站熄灭，*  
*文明的知识仍在手中传承。*

</div>

---

## 🌑 项目概念

> *"The Ark is not an escape. It is a seed."*

**ARK** 是一个为**后网络时代**设计的离线知识生存终端。

它不依赖任何外部基础设施——不需要信号塔、不需要电网、不需要云服务器。它是一个完全自给自足的**数字文明节点**，将人类数千年的核心知识封装在一个手掌可握的装置中，并赋予它本地AI的思考能力。

```
┌─────────────────────────────────────────────────────┐
│  ☀️ 太阳能供电    →    🔋 储能系统    →    📱 计算核心  │
│         ↓                                              │
│    ┌──────────────────────────────────────┐           │
│    │  🧠 本地LLM  │  📚 离线百科  │  🗺️ 离线地图  │           │
│    │  🏥 医疗急救  │  🔧 技术手册  │  🌱 生存指南  │           │
│    └──────────────────────────────────────┘           │
└─────────────────────────────────────────────────────┘
```

---

## ⚡ 核心能力

| 能力域 | 功能描述 | 数据规模 |
|--------|----------|----------|
| **🧠 本地AI推理** | 离线运行Llama-3-8B大模型，支持问答、分析、决策辅助 | ~5GB |
| **🏥 医疗急救** | 离线医学百科、急救流程、药物参考、手术基础 | ~1.2GB |
| **🔧 技术修复** | 机械、电子、建筑、能源系统维修知识库 | ~2GB |
| **🌱 生存技能** | 野外生存、农业种植、净水、食物保存 | ~1GB |
| **🗺️ 离线导航** | 省级离线地图、地形数据、GPS定位 | ~3.5GB |
| **📖 数字图书馆** | 技术手册、工具书、参考资料epub/pdf | ~2GB |

---

## 🛠️ 技术架构

### 硬件平台
```yaml
Core: OnePlus 8T (KB2000)
SoC: Qualcomm Snapdragon 865 (7nm)
RAM: 12GB LPDDR5
Storage: 256GB UFS 3.1 + 1TB extensible
Display: 6.55" AMOLED 120Hz
Power: 4500mAh internal + 20000mAh external + 20W solar
OS: LineageOS 20 + Termux + Debian Container
```

### 软件栈
```
┌─────────────────────────────────────────┐
│  应用层：Kiwix-Serve / OsmAnd / Llama.cpp  │
├─────────────────────────────────────────┤
│  容器层：Debian 12 (Andronix)            │
├─────────────────────────────────────────┤
│  终端层：Termux + Termux:API             │
├─────────────────────────────────────────┤
│  系统层：LineageOS 20 (Android 13)       │
└─────────────────────────────────────────┘
```

### 3D打印外壳
- **材质**: PETG/ASA 耐紫外线
- **防护**: IP54 防尘防泼溅
- **结构**: 双层减震 + 被动散热风道
- **集成**: 太阳能板折叠支架一体化设计

---

## 🚀 快速开始

### 1. 硬件准备
- [📋 硬件配置清单](./docs/hardware/config.md) - 完整BOM表与采购指南
- [🔧 3D打印文件](./docs/hardware/config.md#3d打印文件规格) - STL模型与打印参数

### 2. 系统部署
```bash
# 刷入 LineageOS（可选但推荐）
# 安装 Termux (F-Droid版本)
# 通过 Andronix 部署 Debian 容器
# 部署 llama.cpp + Kiwix-Serve + OsmAnd
```

### 3. 查看原型
打开 [3D原型展示](./docs/design/index.html) 在浏览器中查看交互式原型。

---

## 📊 项目状态

| 模块 | 状态 | 备注 |
|------|------|------|
| 硬件集成 | 🔧 构建中 | 3D打印外壳设计中 |
| 系统部署 | ✅ 已完成 | Termux + Debian 容器 |
| 本地AI | ✅ 已完成 | llama.cpp 运行验证 |
| 知识库 | 📥 收集中 | WikiMed + Appropedia |
| 离线地图 | ⏳ 待测试 | OsmAnd 省级地图包 |
| 外壳设计 | 🎨 进行中 | 参数化CAD建模 |

---

## 🌍 为什么是 ARK？

```
    ╔═══════════════════════════════════════════════╗
    ║                                               ║
    ║   当灾难来临时，                               ║
    ║   搜索引擎会沉默，                             ║
    ║   云端会失联，                                 ║
    ║   但 ARK 会一直运行。                          ║
    ║                                               ║
    ║   它不只是一台设备，                           ║
    ║   它是文明知识的火种，                         ║
    ║   等待被传承。                                 ║
    ║                                               ║
    ╚═══════════════════════════════════════════════╝
```

---

## 📜 文档导航

### 📂 项目结构
```
Ark/
├── README.md                 # 项目主页
├── LICENSE                   # MIT许可证
├── docs/                     # 文档目录
│   ├── hardware/             # 硬件文档
│   │   ├── config.md        # 配置清单
│   │   └── assembly-guide.md # 组装指南
│   ├── software/             # 软件文档
│   │   ├── deployment.md    # 部署教程
│   │   ├── termux-setup.md  # Termux配置
│   │   └── data-sources.md  # 数据来源
│   └── design/               # 设计原型
│       └── index.html       # 3D交互原型
├── assets/                   # 静态资源
│   ├── images/              # 图片
│   ├── css/                 # 样式文件
│   └── js/                  # 脚本文件
├── src/                      # 源代码
│   ├── scripts/             # 自动化脚本
│   └── configs/             # 配置文件
└── data/                     # 数据目录
    ├── kiwix-packages/      # 离线百科
    ├── maps/                # 离线地图
    └── ai-models/           # AI模型文件
```

### 📖 快速导航
- [� 硬件配置清单](./docs/hardware/config.md) - BOM表与采购
- [🎨 3D原型展示](./docs/design/index.html) - 交互式可视化
- [⚙️ 部署指南](./docs/software/deployment.md) - 系统搭建教程
- [📚 数据来源](./docs/software/data-sources.md) - 知识库清单

---

<div align="center">

**[ARK] ▲ Offline Knowledge Survival Node**  
*Built for the unknowable future.*

</div>