# Google Pixel 2 xl update Android 11 & root


9号起床，收到邮件通知
> check out these new Pixel features

![](../../imgs/note/phone/2020-09-09_154537.png)

看到推特上，John Wu 也更新了 root 成功的截图。准备 ~ 开搞！

![](../../imgs/note/phone/2020-09-09_100232.png)

## 备份

- 微信导出（微信PC）
- 备份联系人、备份短信、备份通话记录 （QQ同步助手）
- 备份WiFi连接（钛备份）
- 钛备份所有app（钛备份）
- SD卡内容导出（HandShaker）

## 系统下载

谷歌官方手机系统下载地址:

[https://developers.google.com/android/images#taimen](https://developers.google.com/android/images#taimen)   (原版)

[https://developers.google.cn/android/images#taimen](https://developers.google.cn/android/images#taimen)  （国内 免翻墙下载）

## 驱动下载

[https://developer.android.com/studio/run/win-usb](https://developer.android.com/studio/run/win-usb) （adb 线刷驱动）

adb-fastboot-v4

[https://pan.baidu.com/s/1Lk1xYFvg9lxKpjZt-N9wcw](https://pan.baidu.com/s/1Lk1xYFvg9lxKpjZt-N9wcw)

## 升级工具下载

- [https://twrp.me/Devices/](https://twrp.me/Devices/) (下载地址 设备搜索)
- [twrp-3.4.0-1-taimen.img](https://eu.dl.twrp.me/taimen/twrp-3.4.0-1-taimen.img)
- [https://magisk.cc/](https://magisk.cc/ ) （magisk 下载地址 国内源地址）
- [https://magisk.cc/magisk_files.php?type=debug](https://magisk.cc/magisk_files.php?type=debug ) （debug版本下载地址）

## 系统解压
**taimen-rp1a.200720.009-factory-f2d162ef.zip**

- image-taimen-rp1a.200720.009.zip
    - boot.img
    - dtbo.img
    - system.img
    - system_other.img
    - vbmeta.img
    - vendor.img

**bootloader-taimen-tmz30m.img**

**radio-taimen-g8998-00034-2006052136.img**

## 刷入 recovery.img
```shell
fastboot flash boot twrp-3.4.0-1-taimen.img
```

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