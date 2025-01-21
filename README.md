# Cursor Pro 自动化工具使用说明

README also avaiable in: [English](./README.EN.md), [Tiếng Việt](./README.VI.md)

## 功能介绍
自动注册账号、自动刷新 token，解放双手。

## 下载地址
[https://github.com/chendeben/cursor-auto-free/releases](https://github.com/chendeben/cursor-auto-free/releases)

## 重要说明
1. **请确保已安装 Chrome 浏览器。如果没有，请[点击此处下载](https://www.google.com/intl/zh-CN/chrome/)**
2. **需要登录账号，无论账号是否有效，登录是必须的**
3. **需要稳定的网络连接，优先使用国外服务器。请勿开启全局代理**

## 配置说明
可以不做任何配置直接使用
下载 .env.example 文件到程序所在根目录，并重命名为 .env 文件。

## 运行方法
### 各平台版本使用说明
#### 环境变量配置

在 `.env` 文件中可以配置以下选项：

```bash
# 可选配置
HEADLESS=true       # 启用无头模式（默认：false）
PROXY='http://127.0.0.1:7890'  # 代理服务器地址（可选）
```

本项目修改自 [gpt-cursor-auto](https://github.com/chengazhen/cursor-auto-free)，修改了获取邮件部分，内置邮件系统API，不再需要配置邮件相关，自动使用临时邮件来获取验证码。

## 更新日志
- **2025-01-09**: 添加日志和自动构建功能
- **2025-01-10**: 优化邮件配置
- **2025-01-11**: 通过 .env 文件添加无头模式和代理配置
- **2025-01-21**: 移除邮件配置要求

