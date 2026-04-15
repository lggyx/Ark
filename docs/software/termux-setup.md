# Termux 环境配置

> 🚧 本文档正在编写中...

## 安装 Termux

从 F-Droid 下载安装（推荐）：
- https://f-droid.org/packages/com.termux/

## 基础配置

```bash
# 更新软件源
pkg update && pkg upgrade

# 安装基础工具
pkg install git curl wget vim

# 安装 Termux:API
pkg install termux-api
```

## 存储权限

```bash
# 获取存储权限
termux-setup-storage

# 创建项目目录
mkdir -p ~/Ark/{data,scripts,configs}
```

## 后续步骤

参考 [部署指南](./deployment.md) 继续配置。

---

*最后更新: 2026-04-15*
