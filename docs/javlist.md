<link rel="stylesheet" href="https://www.layuicdn.com/layui/css/layui.css"  media="all">
<table class="layui-hide" id="test"></table>
<script src="https://www.layuicdn.com/layui/layui.js" charset="utf-8"></script>
<script src="https://code.getmdl.io/1.3.0/material.min.js"></script>


 
<script>
layui.use('table', function(){
  var table = layui.table;
  
  table.render({
    elem: '#test'
    ,url:'https://hi-andy.com/files/jav_data.json'
    ,cellMinWidth: 80 //全局定义常规单元格的最小宽度，layui 2.2.1 新增
    ,cols: [[
      {field:'id', width:110, title: '番号', sort: true}
      ,{field:'name', width:125, title: '演员', sort: true}
      ,{field:'jav', width:290, title: '名称'}
      ,{field:'score', width:75, title: '评分', sort: true}
      ,{field:'date', width:150, title: '发行日期', sort: true}
    ]]
  });
});
</script>

