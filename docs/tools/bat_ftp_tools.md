# 批处理 ftp 一键下载上传工具 V 1.1.0

工具打包下载  [批处理ftp 一键下载上传工具V1.1.0](../files/bat_ftp_tools.zip)

> 使用说明：<br>
　注：不支持批量文件上传、下载，目前只支持单文件下载功能。<br>
【上传功能】<br>
　0. 手动修改 gjzqftp_upload.bat 修改为自己得用户名和密码<br>
　1. 管理员身份运行，install【管理员运行】.bat<br>
【下载功能】<br>
　0. 手动修改 gjzqftp_download.bat 修改为自己得用户名和密码<br>
　1. 在ftp根目录创建download目录（下载逻辑是从此目录下载，下载后清空）<br>
　2. 注:下载后会自动删除ftp目录内文件! 请注意<br>
　3. 下载默认路径为桌面（可手动修改路径ftp_path）<br>
【日志】<br>
　文件上传/下载日志存在：D:/ftp.log 

## 上传功能

```bash
@echo off
REM # Title:         ftp文件上传工具
REM # Description:   拖动文件上传
REM # Author:        andyhou  <andy@hi-andy.com>
REM # Date:          2020-12-30
REM # Version:       1.1.0
REM # tips：使用方法是将文件拖到批处理脚本上门/或者绑定右键菜单上传。

set server=IP
set username=用户名
REM 密码中包含特殊符号，在之前加“^”符号进行转义，例如：123@123 为 123^@123
set password=密码
set file=%1
set logs=D:/ftp.log

echo user %username%> ftpcmd.dat
echo %password%>> ftpcmd.dat
echo put %file%>> ftpcmd.dat
echo quit>> ftpcmd.dat
ftp -n -s:ftpcmd.dat %server%
del ftpcmd.dat
echo %date:~0,4%-%date:~5,2%-%date:~8,2% %time% 上传"%file%"到ftp服务器 %server% >> %logs%
```

## 上传功能的升级，加入右键菜单

![2021-01-08_155827](\imgs\tools\2021-01-08_155827.png)

用注册表将批处理上传功能注册！保存为"ftp上传脚本注册右键显示.reg"

```Reg
Windows Registry Editor Version 5.00

[HKEY_CLASSES_ROOT\*\shell\GJZQ_Upload_FTP]
@="上传文件到Gjzqftp"

[HKEY_CLASSES_ROOT\*\shell\GJZQ_Upload_FTP\command]
@="\"C:\\Windows\\gjzqftp_upload.bat\" \"%1\""
```

一键安装拷贝注册脚本

```bash
@echo off
copy %~dp0\gjzqftp_upload.bat C:\Windows\
regedit /s %~dp0\ftp上传脚本注册右键显示.reg

pause
```

## 下载功能

```BAT
@echo off
REM # Title:         ftp文件下载工具
REM # Description:   执行下载最新文件
REM # Author:        andyhou  <andy@hi-andy.com>
REM # Date:          2020-12-30
REM # Version:       1.1.0
REM # tips：使用方法是执行右键下载/或者绑定右键菜单下载。

set "ftp_ip=IP"
set "ftp_user=用户名"
REM 密码中包含特殊符号，在之前加“^”符号进行转义，例如：123@123 为 123^@123
set "ftp_pass=密码"
REM 指定下载路径，默认指定桌面
set "ftp_path=%USERPROFILE%\Desktop"
set logs=D:/ftp.log

echo open %ftp_ip% > ftpcmd.dat
echo user %ftp_user% >> ftpcmd.dat
echo %ftp_pass%>> ftpcmd.dat
echo prompt >> ftpcmd.dat
echo binary >> ftpcmd.dat
echo cd download >> ftpcmd.dat
echo ls . ftplist.dat >> ftpcmd.dat
echo lcd %f_tmp% >> ftpcmd.dat
echo disconnect >> ftpcmd.dat
echo bye >> ftpcmd.dat

ftp -v -n -s:ftpcmd.dat


for /f "delims=" %%i in ('type "ftplist.dat"') do (
    set "dowload_file=%%i"
)

echo open %ftp_ip% > ftpcmd.dat
echo user %ftp_user% >> ftpcmd.dat
echo %ftp_pass%>> ftpcmd.dat
echo prompt >> ftpcmd.dat
echo binary >> ftpcmd.dat
echo cd download >> ftpcmd.dat
echo lcd %f_tmp% >> ftpcmd.dat
echo get "%dowload_file%" "%ftp_path%\%dowload_file%" >> ftpcmd.dat
echo del %dowload_file% >> ftpcmd.dat
echo disconnect >> ftpcmd.dat
echo bye >> ftpcmd.dat
ftp -v -n -s:ftpcmd.dat
del ftpcmd.dat
del ftplist.dat
echo %date:~0,4%-%date:~5,2%-%date:~8,2% %time% 从ftp服务器 %ftp_ip%下载"%dowload_file%" >> %logs%
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

