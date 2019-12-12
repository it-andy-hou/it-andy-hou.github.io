# Google Nexus6P android 8.1 & root 刷机流程

### 备份

- 微信导出
- 备份联系人
- 备份通话记录
- 备份WiFi连接
- 备份短信
- 钛备份所有app
- SD卡内容导出

### 系统下载

https://developers.google.com/android/images

### xposed

| 系统版本 | API  | 备注                                                         |
| -------- | ---- | ------------------------------------------------------------ |
| 8.1      | 27   | https://dl-xda.xposed.info/framework/sdk27/arm64/xposed-v90-sdk27-arm64-beta3.zip |
| 8.0      | 26   |                                                              |
| 7.1      | 25   |                                                              |
| 7.0      | 24   |                                                              |
| 6.0      | 23   |                                                              |

卸载包地址：https://dl-xda.xposed.info/framework/uninstaller/xposed-uninstaller-20180117-x86.zip

https://dl-xda.xposed.info/framework/

### 驱动

https://developer.android.com/studio/run/win-usb

### SU 下载

https://autoroot.chainfire.eu/

https://desktop.firmware.mobi/

`fastboot flash boot boot.img`

### twrp

https://dl.twrp.me/angler/

### GAPPS

http://downloads.codefi.re/jdcteam/javelinanddart/gapps

https://opengapps.org/?api=8.1&variant=nano

https://wiki.lineageos.org/gapps.html

### 刷机命令

```bash
fastboot flash bootloader bootloader-hammerhead-hhz12h.img
fastboot flash radio radio-hammerhead-m8974a-2.0.50.2.26.img
fastboot reboot-bootloader
 
fastboot flash recovery recovery.img
fastboot flash boot boot.img
fastboot flash system system.img

fastboot flash vendor vendor.img

fastboot flash cache cache.img
fastboot flash userdata userdata.img
```

## magisk

https://forum.xda-developers.com/apps/magisk

- Magisk-v17.3
- MagiskManager-v6.0.1