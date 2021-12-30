# 腾讯云堡垒机开启二次（双因素）验证，xshell自动登录脚本

## 效果
<iframe width="900" height="600" src="//player.bilibili.com/player.html?aid=550208735&bvid=BV1Ui4y1R7ep&cid=471526416&page=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"> </iframe>
**xshell 弹窗 密码输入框没有录进去，请忽略。**

依赖项目:
GitHub:[https://github.com/ms2008/Xshell-OTP](https://github.com/ms2008/Xshell-OTP)

## 原理

> 使用 [Google Authenticator](https://chrome.google.com/webstore/detail/authenticator/bhghoamapcdpbohphigoooaddinpkbai) MFA 验证机制登录跳板机，可以通过其导出的 secret 在本地计算出当前的 token。Xshell 支持运行 javascript 脚本，所以这个 token 可以直接在 Xshell 端计算完成。但是 Xshell 在处理 MFA 验证机制时，是直接弹出对话框，并不支持传统的 terminal 输入，Xshell 也并没有提供自动完成的 API，所以只能手动拷贝输入。

- 只支持腾讯云**传统型堡垒机** （版本 **TC_3.0.11.10** 以上）

腾讯云堡垒机使用起来确认是没有 阿里云上额堡垒机方便，在Windows上的支持也不是很好，现有市场上做的好的大概是 “齐治”的堡垒机，我觉得云厂商抓紧时间抄一下啊。



## 操作步骤

**提取到 MFA验证的secret值** ，这步请参考 我之前写过的 ["插件 Authenticator(身份验证器)"](https://hi-andy.com/tools/Chrome_Plugins_Authenticator/),用插件提取出 **secret值** 

<img src="/imgs/note/2021/2021-12-29_163855.png">

导出后会下载到 **authenticator.txt** 文本，打开后就能看到 secret= 后面的数值，复制出来

使用 **Xshell-OTP** 项目提供的 **jumper.js** ，修改代码

```javascript
2326行   var otp = totpObj.getOTP("这里填写提取到 MFA验证的secret值");
```

```javascript
// 这行是调用cmd将密码复制进粘贴板里，方便粘贴到xhsell 弹窗里
xsh.Screen.Send("cmd /c echo " + otp + "| clip");
```

适配腾讯云堡垒机，腾讯堡垒机是用户密码+OTP的形式。
```javascript
//适配腾讯云堡垒机
xsh.Screen.Send("cmd /c echo " +"用户密码"+ otp + "| clip");
```

以上就完成了腾讯云堡垒机的自动登录操作步骤，至于内部菜单，可以通过自己编写vbs来直接跳转到对应机器上。




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