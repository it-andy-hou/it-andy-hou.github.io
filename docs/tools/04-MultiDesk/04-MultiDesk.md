# 🌟 Windows 远程桌面连接神器 MultiDesk 

<div style="width:100%;max-width:100%;height:500px;overflow-x:auto;overflow-y:hidden;white-space:nowrap;display:flex;align-items:center;">
  <img src="/tools/04-MultiDesk/multidesk_1.chs.png" alt="Image 1" style="height:100%;margin-right:10px;">
  <img src="/tools/04-MultiDesk/multidesk_7.chs.png" alt="Image 2" style="height:100%;margin-right:10px;">
  <img src="/tools/04-MultiDesk/multidesk_8.chs.png" alt="Image 3" style="height:100%;margin-right:10px;">
  <img src="/tools/04-MultiDesk/multidesk_9.chs.png" alt="Image 4" style="height:100%;margin-right:10px;">
  <img src="/tools/04-MultiDesk/multidesk_10.chs.png" alt="Image 5" style="height:100%;margin-right:10px;">
</div>

## 什么是 MultiDesk?
MultiDesk 是一个选项卡（TAB标签）方式的远程桌面连接 (Terminal Services Client)。

## 功能特性
- 绿色软件，只有一个很小的可执行文件，采用 C++ 编写，运行速度快!
- 支持 RDP over VMBus (Hyper-V)
- 支持网络唤醒
- 支持 SOCKS5 代理
- 支持导入 MSTSC 的连接
- 支持通过扫描网络来快速导入服务器
- 支持使用主密码来加密服务器登录密码
- 支持 Start Program (官方 Windows 10 自带的 MSTSC 已不再支持)
- 支持 Remote Desktop Gateway
- 支持在连接后输入用户名和密码
- 支持连接到控制台
- 支持设置连接端口
- 支持重定向指定的驱动器
- 支持快速连接
- 支持快速全屏幕分辨率切换
- 针对固态硬盘(SSD)、闪存盘专门优化设计，最大限度减少写盘
- 新风格：隐藏标题栏，状态栏和带有边界的自适应窗口
- 选项卡(TAB 标签)方式，可以使用快捷键切换
- 使用分组模式进行管理
- 支持从分组属性继承设置
- 支持对分组、服务器拖放操作
- 支持从 Windows XP/Server 2003 开始的全部 Windows 系统
- 支持高分屏/自定义缩放级别（需要 Windows 10; Server 2016）
- 支持自定义外部工具
- 支持智能滚动

## 版本
免费版（限制2个并发连接）
捐赠者专用版。（捐赠者专用版支持无限并发连接，大于10块钱就行）

## 评价
使用了很多年，非常稳定，推荐。管理上百台Windows服务器，用这个工具非常方便。另外十几块是买个安心，支持一下独立开发作者。

## 私货推荐
因为服务器密码都是存在注册表中，所以可以写个脚本，把注册表中的密码读导出
reg export "HKEY_CURRENT_USER\Software\MultiDesk" "MultiDesk.reg"
密码导入命令
reg import "MultiDesk.reg"

## 获取方式
[https://www.syvik.com/multidesk/index.cn.html](https://www.syvik.com/multidesk/index.cn.html)


> 标签： #程序员 #运维 #开发工具 #远程桌面 #效率工具 #技术分享 #编程 #Windows