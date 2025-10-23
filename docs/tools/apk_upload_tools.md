# 批处理 + Server端 文件传输工具

工具打包下载  [上传远程服务器工具 V1.0](../files/apk_upload_tools.zip)

## 后端实现原理
apache cgi 功能实现，具体还是不阐述了。

## 目录文件
```
apk_upload_tools
├─ apk_upload.bat
├─ apk上传脚本注册右键显示.reg
├─ install【管理员运行】.bat
└─ server
       ├─ files_auto_ff.sh
       ├─ files_check.sh
       └─ files_upload.py
```

## 常规入口（右键菜单）
![2021-05-13_153619.png](\imgs\tools\2021-05-13_153619.png)


## 整体功能结构图 
![apk_upload_tools.png](\imgs\tools\apk_upload_tools.png)

用户打包完成后，通过右键直接上传的方式，直接讲文件推送到指定分类的目录下。

脚本代码方面我就不多做说明，毕竟可以下载查看到，理论上可以再简化一下，来替代 ‘rz’ 的功能。然后传参指定IP，还是能提高一下工作效率，当然还是要分不同的应用场景，可以再自己定制一下，事半功倍。



<hr>

<script src="https://utteranc.es/client.js"
        repo="it-andy-hou/it-andy-hou.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
