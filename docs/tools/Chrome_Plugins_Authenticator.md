# 插件 Authenticator(身份验证器)

<img width="150" src="https://authenticator.cc/assets/logo/logo.svg"> </img>

## **插件支持浏览器**

- Chrome
- Firefox
- Edge

## **关键特性**

- **通过扫描二维码添加账号**
- 使用密码加密数据
- 在浏览器之间同步数据
- 备份数据到云服务或导出数据到文件
- 智能过滤和搜索

官网地址: [https://authenticator.cc/](https://authenticator.cc/)

官方说明文档：[https://authenticator.cc/docs/en/overview](https://authenticator.cc/docs/en/overview)

## **插件下载**

chrome应用市场地址： [https://chrome.google.com/webstore/detail/authenticator/](https://chrome.google.com/webstore/detail/authenticator/bhghoamapcdpbohphigoooaddinpkbai?hl=zh-CN)

如果你因为网络问题无法访问，可以通过下面方式获取。

可以直接下载离线 [https://crxdl.com/](https://crxdl.com/) （程序ID **bhghoamapcdpbohphigoooaddinpkbai**）

## **使用说明**
1. 首先已经手机端安装了 "Google 身份验证器" 且已经绑定了二次验证码，我们操作其实就是把手机的二次验证码复制到PC上，迁移的原因...不知道有没有在电脑前办公的时候，不想再掏出手机点开应用记住验证码再输入到电脑上，最好是直接再PC上操作，这个插件的左右便是如此。
2. 我们可能**需要第二台手机协助一下**，因为"Google 身份验证器"在导出二维码的时候，是**不允许手机截屏的**，所以只能拍下来完成导出。(导出可以选择全部导出和部分导出，根据自己实际需要)<br>
![2021-09-15_135954](\imgs\tools\2021-09-15_135954.png)
3. 将导出的图片传到电脑上，然后安装好插件，复制下面地址到浏览器
```
chrome-extension://bhghoamapcdpbohphigoooaddinpkbai/view/import.html?QrImport
```
然后选择"导入QR图片备份" 选择对应的二维码照片
![2021-09-15_140925](\imgs\tools\2021-09-15_140925.png)
导入完成就成功了，点击插件按钮就会弹出对应的验证码了。

![2021-09-14_173930](\imgs\tools\2021-09-14_173930.png)

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