L2Dwidget.init({
    "model": {
        // http://demo.frontendx.cn/live2d-example/index.html 示例 cdn搜索 https://www.jsdelivr.com/?query=hijiki
        jsonPath: "https://cdn.jsdelivr.net/npm/live2d-widget-model-hijiki@1.0.5/assets/hijiki.model.json",
        "scale": 1
    },
    "display": {
        "position": "left",
        "width": 100,
        "height": 220,
        "hOffset": 10,
        "vOffset": -100
    },
    "mobile": {
        "show": true,
        "scale": 0.5
    },
    "react": {
        "opacityDefault": 0.8,
        "opacityOnHover": 0.2
    }
});
