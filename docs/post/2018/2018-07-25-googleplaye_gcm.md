---
id: 746
title: GooglePlay版微信省电，稳定接收GCM2
date: 2018-07-25T00:08:17+00:00
author: andy
layout: post
guid: https://hi-andy.com/?p=746
permalink: /746.html
image: /wp-content/uploads/2018/07/gcm.jpg
categories:
  - Android
  - FQ
---
# 微信 稳定接收 GCM

**Google Cloud Messaging（GCM）**是一项免费服务，可让开发人员在服务器和客户端应用之间发送消息。这包括从服务器到客户端应用的下游消息，以及从客户端应用到服务器的上游消息。
> 截至2018年4月10日，Google已弃用GCM。GCM服务器和客户端API已弃用，将于2019年4月11日删除。将GCM应用程序迁移到Firebase云消息传递（FCM），后者继承了可靠且可扩展的GCM基础架构以及许多新功能。请参阅 迁移指南以了解更多信息。

https://developers.google.com/cloud-messaging/

**Firebase 云信息传递 (FCM)** 是一种跨平台消息传递解决方案，可供您免费、可靠地传递消息。

https://firebase.google.com/docs/cloud-messaging/

> **Android的微信智能心跳方案**： https://mp.weixin.qq.com/s/ghnmC8709DvnhieQhkLJpA (失效可以搜索标题，查看其他转载 )
> 文章写的比较早15年8月，但对GCM的分析还是比较透彻的，有助与理解GCM的策略和机制。
&gt;
> **关于 Android 通知推送，你需要知道这些事 | 科普** ：https://sspai.com/post/42573

上面是科普系列，我觉得玩Android久的大多都应该知道，这里我也就不过多废话了。Google 的公告也说明了，GCM支持到19年4月，所以在此之间还是通过GCM来完成整套解决方案，主要也是目前的APP也都是GCM。

**目前需求**

- 省电！省电！还是省电
- Android 8.1 ( Nexus 6P lineageos 15.1 )
- 解决微信的耗电问题,像IOS 接收微信！(MD!)

**解决方案**

- 纯净的 Android OS ( lineageos ) [Install LineageOS on angler](https://wiki.lineageos.org/devices/angler/install)
- **Xposed** [ XposedInstaller](https://forum.xda-developers.com/showthread.php?t=3034811)、[xposed\*.zip](https://dl-xda.xposed.info/framework/)
- **Root** [su(for lineageos)](https://download.lineageos.org/extras)
- **Google Play Service** [Google apps](https://wiki.lineageos.org/gapps.html)
- [**Google Play 的微信**](https://play.google.com/store/apps/details?id=com.tencent.mm)
- **应用管理 X-APM** [项目地址]( https://github.com/Tornaco/X-APM) 、[GCM消息代收](https://github.com/Tornaco/X-APM/wiki/GCM%E6%B6%88%E6%81%AF%E4%BB%A3%E6%94%B6)
- **PNF Root** [Root- Push Notifications Fixer](https://play.google.com/store/apps/details?id=com.andqlimax.pushfixer)
- [Shadowsocks](https://play.google.com/store/apps/details?id=com.github.shadowsocks)
- [Override DNS](https://play.google.com/store/apps/details?id=net.mx17.overridedns)
- Hosts
- [黑阈](https://play.google.com/store/apps/details?id=me.piebridge.brevent)
- [绿色守护](https://play.google.com/store/apps/details?id=com.oasisfeng.greenify)
- [BetterBatteryStats](https://play.google.com/store/apps/details?id=com.asksven.betterbatterystats)
- 需要好友协助微信测试

 以上为需要的应用或者服务，看上去有点多还有点懵逼，主要是包含了几个过渡解决方案，加粗为必须的项目。核心是**应用管理 X-APM** 提供的微信GCM代收服务，我才打算搞定这套东西，之前的绿色守护也能实现GCM的接收，但是一直都不是很稳定。
你要问我 Nexus 6P 为什么不用原生系统，刷LOS 我的回答就是因为要省电，原生太多Google 服务，当然也可以通过**系统卸载器**来卸载掉不用的Google 应用或者服务，后者干脆停用。要是我说我觉得我唯一觉得就是原生系统的相机是我无法割舍的。剩下我觉得LOS都可以代替。（刷机这套东西我有空再写套教程吧）
​ 其实在测试上面的方案时候，我还查了一大堆资料或者寻找替代方案，[**MiPushFramework**](https://github.com/Trumeet/MiPushFramework) （在任何非 MIUI 设备上体验小米系统级推送。）其实我觉得这个项目还是不错的，主要是因为兼容性没能在我的设备上正常运行，决定放弃了，如果有兼容的机型或者系统我觉得可以考虑的。这个服务需要 **[Magisk](https://github.com/topjohnwu/Magisk)** 框架支持实现设备改名字有些APP会读取设备名称，改成小米的设备。正因为这些我觉得放弃这个方案。而且Magisk 和 Xposed 好像有点冲突。
​ 中间还搜索到相关**[sjdy521](https://github.com/sjdy521)** 写的项目 [Mojo-Webqq](https://github.com/sjdy521/Mojo-Webqq)、[Mojo-Weixin](https://github.com/sjdy521/Mojo-Weixin)、 [GcmForMojo](https://www.coolapk.com/apk/com.swjtu.gcmformojo)

**具体操作**
​ 前面的ROOT、Xposed、Google Play service(我记得有个Google服务一键安装的) 和手机翻墙我就不具体强调怎么搞了。
​ 应用**应用管理 X-APM** 安装完成后就有一个选项可以开启，微信GCM的设置参照 http://www.oneplusbbs.com/thread-4078080-1.html 我也不太想重复别人写的，大家自己看。进阶 &gt; GCM 代收 ，需要强调的是需要将微信加入黑阈 和 X-APM的乖巧模式，要保证微信不要后台驻留，要不然进程存在微信还是会用自己的消息提醒机制。
​ 接下来就是要保证稳定的接收到GCM，全网最多的方案就是**后台常开Shadowsocks**，有人说这种方法更傻因为常挂翻墙，那不得更费点，不错从操作逻辑上也算是简单，省电的角度我目前还没有横向对比测试。基本上你开启Shadowsocks就可以找朋友测试 微信的GCM服务来接收消息了。关于调试**BetterBatteryStats**、**PNF Root** 这两个应用是用来调试的，前者是耗电统计的，主要是统计GCM 耗电量问题，**PNF Root** 则是可以修改GCM心跳间隔的，查看GCM连通日志。这里说一个快捷操作`*#*#426#*#*`同样可以常看GCM的连接情况和日志。以上就是用 **Shadowsocks的方案**。
​ Hosts方案，hosts 这个大家应该也不陌生，用hosts 翻墙的方法大家应该也都懂我这里不过多说操作，hosts 的方案就是 将GCM的服务写入hosts这个方案存在时效性，被封了就不能及时收到消息，但是相比较上面的方案更省电因为是直连不用开服务。关于Hosts 文件》[Google Hosts 项目](https://github.com/googlehosts/hosts)

```ini
# Google:gcm Start
108.177.97.188 mobile-gtalk.l.google.com
108.177.97.188 mtalk.google.com
108.177.97.188 mtalk4.google.com
108.177.97.188 gcm.googleapis.com
108.177.97.188 gcm.l.google.com
108.177.97.188 gcm-xmpp.googleapis.com
108.177.97.188 gcm-preprod.l.google.com
108.177.97.188 gcm-preprod.googleapis.com
216.58.199.10 gcm-http.googleapis.com
# Google:gcm End
```
 最后的方案其实可以和Hosts 的方案同时使用，其实你不难发现这些方案就是平时FQ的方案。最后的方案就是DNS的解析方案。Override DNS 我是使用这个软件来修改DNS的，当然你也可以通过其他软件，大部分都是需要root权限的。原理其实和上面的一样，通过无污染的DNS来正常解析GCM服务器，这里的DNS服务器我就不列举了。

关于各种FQ的软件汇总我也曾经写过一个 https://github.com/it-andy-hou/fq 大家可以参考。