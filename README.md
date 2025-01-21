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

## 运行方法

### Mac 版本
1. 打开终端，进入应用所在目录
2. 运行命令：授权文件可以执行
```bash
chmod +x ./CursorPro
```
3. 运行程序：
   - 在终端中运行：
```bash
./CursorPro
```
   - 或直接在访达（Finder）中双击运行


提示：如果遇到下面的问题; [解决方案](https://sysin.org/blog/macos-if-crashes-when-opening/)


![image](./screen/c29ea438-ee74-4ba1-bbf6-25e622cdfad5.png)



### Windows 版本
直接双击运行 `CursorPro.exe`


## 如何验证是否有效
**运行脚本完成之后，重启你的编辑器，你会看到下面图片的账号和你的脚本输出的日志账号一致就搞定了。**
![image](./screen/截屏2025-01-04%2009.44.48.png)


本项目修改自 [gpt-cursor-auto](https://github.com/chengazhen/cursor-auto-free)，修改了获取邮件部分，内置邮件系统API，不再需要配置邮件相关，自动使用临时邮件来获取验证码。

## 更新日志
- **2025-01-21**: 移除配置要求

