# Google Pixel 2 xl update Android 10 & root

## 备份

- 微信导出（微信PC）
- 备份联系人、备份短信、备份通话记录 （QQ同步助手）
- 备份WiFi连接（钛备份）
- 钛备份所有app（钛备份）
- SD卡内容导出（HandShaker）

## 系统下载

谷歌官方手机系统下载地址:

https://developers.google.com/android/images#taimen   (原版)

https://developers.google.cn/android/images#taimen  （国内 免翻墙下载）

## 驱动下载

https://developer.android.com/studio/run/win-usb （adb 线刷驱动）

adb-fastboot-v4

https://pan.baidu.com/s/1Lk1xYFvg9lxKpjZt-N9wcw

## 升级工具下载

- [twrp-3.3.0-0-taimen.img](https://eu.dl.twrp.me/taimen/twrp-3.3.0-0-taimen.img.html)

- [twrp-pixel2-installer-taimen-3.3.0-0.zip](https://eu.dl.twrp.me/taimen/twrp-pixel2-installer-taimen-3.3.0-0.zip.html)

- Magisk-v19.3.zip

  https://forum.xda-developers.com/apps/magisk/official-magisk-v7-universal-systemless-t3473445

- [Magisk Manager v7.3.2](https://github.com/topjohnwu/Magisk/releases/tag/manager-v7.3.2)

  https://github.com/topjohnwu/Magisk/releases
  
- https://github.com/topjohnwu/magisk_files/tree/master/canary_builds

## 系统解压

解压 taimen-qp1a.190711.020-factory-6f0233dd.zip   *10.0.0 (QP1A.190711.020, Sep 2019)*

- **image-taimen-qp1a.190711.020.zip** 
  - boot.img
  - dtbo.img
  - system.img
  - system_other.img
  - vbmeta.img
  - vendor.img
- **bootloader-taimen-tmz30h.img**
- **radio-taimen-g8998-00012-1905270706.img**
- flash-all.bat
- flash-all.sh
- flash-base.sh

```bat
@ECHO OFF

PATH=%PATH%;"%SYSTEMROOT%\System32"
fastboot flash bootloader bootloader-taimen-tmz30h.img
fastboot reboot-bootloader
ping -n 5 127.0.0.1 >nul
fastboot flash radio radio-taimen-g8998-00012-1905270706.img
fastboot reboot-bootloader
ping -n 5 127.0.0.1 >nul
fastboot update image-taimen-qp1a.190711.020.zip
:: 去掉了w 参数；因为我是重装
echo Press any key to exit...
pause >nul
exit


```

## 刷入 recovery.img

```shell
fastboot flash boot twrp-3.3.0-0-taimen.img
# 真的是好久不刷机，原先recovery 的命令已经变了 。
```

剩下就是install  Magisk-v19.3.zip ；安装APK  懒的写了就这样；Magisk 作者再10正式版出来以后 频繁更新 已经解决了之前遇到坑，这里本来还想提一提，算了。


<hr>

<!-- 来必力City版安装代码 -->
<div id="lv-container" data-id="city" data-uid="MTAyMC80NzA4OC8yMzU4OA==">
	<script type="text/javascript">
   (function(d, s) {
       var j, e = d.getElementsByTagName(s)[0];

       if (typeof LivereTower === 'function') { return; }

       j = d.createElement(s);
       j.src = 'https://cdn-city.livere.com/js/embed.dist.js';
       j.async = true;

       e.parentNode.insertBefore(j, e);
   })(document, 'script');
	</script>
<noscript> 为正常使用来必力评论功能请激活JavaScript</noscript>
</div>
<!-- City版安装代码已完成 -->
