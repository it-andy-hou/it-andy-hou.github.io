<link rel="stylesheet" href="https://www.layuicdn.com/layui/css/layui.css"  media="all">
 
<table class="layui-hide" id="test" style="layui-btn background-color: #333;" lay-filter="test"></table>
 
<script type="text/html" id="toolbarDemo">
  <div class="layui-btn-container">
    <button class="layui-btn layui-btn-sm" lay-event="getCheckData">获取选中行数据</button>
    <!-- <button class="layui-btn layui-btn-sm" lay-event="getCheckLength">获取选中数目</button> -->
    <!-- <button class="layui-btn layui-btn-sm" lay-event="isAll">验证是否全选</button> -->
  </div>
</script>
 
<script type="text/html" id="barDemo">
  <a class="layui-btn layui-btn-xs" lay-event="edit">封面</a>
</script>
              
          
<script src="https://www.layuicdn.com/layui/layui.js" charset="utf-8"></script>
<!-- 注意：如果你直接复制所有代码到本地，上述 JS 路径需要改成你本地的 --> 
 
<script>
layui.use('table', function(){
  var table = layui.table;
  
  table.render({
    elem: '#test'
    // ,url:'http://127.0.0.1:8090/files/jav_data.json'
    ,url:'https://hi-andy.com/files/jav_data.json'
    ,toolbar: '#toolbarDemo' //开启头部工具栏，并为其绑定左侧模板
    ,defaultToolbar: ['filter', 'exports', 'print']
    ,title: '用户数据表'
    ,cols: [[
      {type: 'checkbox', fixed: 'left'}
      ,{field:'id', width:100, title: '番号', sort: true, fixed: 'left'}
      ,{field:'name', width:125, title: '演员', sort: true}
      ,{field:'jav', width:190, title: '名称'}
      ,{field:'date', width:110, title: '发行日期', sort: true}
      ,{field:'time', width:110, title: '观影日期', sort: true,hide:true}
      ,{field:'producers', width:100, title: '发行商', sort: true}
      ,{fixed: 'right',field:'score', width:75, title: '评分', sort: true}
      ,{fixed: 'right', title:'封面', toolbar: '#barDemo', width:70,}
    ]]
  });
  
  //头工具栏事件
  table.on('toolbar(test)', function(obj){
    var checkStatus = table.checkStatus(obj.config.id);
    switch(obj.event){
      case 'getCheckData':
        var data = checkStatus.data;
        layer.alert(JSON.stringify(data));
      break;
      case 'getCheckLength':
        var data = checkStatus.data;
        layer.msg('选中了：'+ data.length + ' 个');
      break;
      case 'isAll':
        layer.msg(checkStatus.isAll ? '全选': '未全选');
      break;
    };
  });
  
  //监听行工具事件
  table.on('tool(test)', function(obj){
    var data = obj.data;
    console.log(data)
    if(obj.event === 'edit'){
        layer.photos({
        photos: {
                "title": "", //相册标题
                "id": 123, //相册id
                "start": 0, //初始显示的图片序号，默认0
                "data": [   //相册包含的图片，数组格式
                  {
                    "alt": data.id + " " +data.jav,
                    "src": data.pics, //原图地址
                  }
                ]
              }
      });
    }
  });
});
</script>
