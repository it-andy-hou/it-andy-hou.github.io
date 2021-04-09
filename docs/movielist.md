<link rel="stylesheet" href="https://www.layuicdn.com/layui/css/layui.css"  media="all">
 
<table class="layui-hide" id="test" style="layui-btn background-color: #333;" lay-filter="test"></table>
 
<table class="layui-table" lay-data="{height:305, url:'http://127.0.0.1:8090/files/movie_data.json', id:'test2', skin: 'row', even: true}">
  <thead>
    <tr>
      <th lay-data="{field:'movie', width:200, templet: '#usernameTpl'}">电影名称</th>
      <th lay-data="{field:'score', width:80, sort: true}">评分</th>
      <th lay-data="{field:'time', width:105, sort: true}">观影日期</th>
      <th lay-data="{field:'review', width:435, height:150, style:'background-color: #eee; color: #000000;'}">短评</th>
    </tr>
  </thead>
</table>

<script type="text/html" id="usernameTpl">
  <a href="{{d.douban}}" class="layui-table-link" target="_blank">{{ d.movie }}</a>
</script>
          
<script src="https://www.layuicdn.com/layui/layui.js" charset="utf-8"></script>
<!-- 注意：如果你直接复制所有代码到本地，上述 JS 路径需要改成你本地的 --> 
 
<script>
layui.use('table', function(){
  var table = layui.table;
});
</script>

  
  