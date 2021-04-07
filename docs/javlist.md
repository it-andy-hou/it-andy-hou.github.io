<link rel="stylesheet" href="https://www.layuicdn.com/layui/css/layui.css"  media="all">
<table class="layui-hide" id="test"></table>
<script src="https://www.layuicdn.com/layui/layui.js" charset="utf-8"></script>

 
<script>
layui.use('table', function(){
  var table = layui.table;
  
  table.render({
    elem: '#test'
    ,url:'https://www.layui.com/demo/table/user/'
    ,cellMinWidth: 80 //全局定义常规单元格的最小宽度，layui 2.2.1 新增
    ,cols: [[
      {field:'id', width:80, title: '番号'}
      ,{field:'name', width:80, title: '演员'}
      ,{field:'jav', width:80, title: '名称', sort: true}
      ,{field:'score', title: '评分', sort: true}
      ,{field:'date', width:80, title: '发行日期'}
      ,{field:'size', title: '大小'}
    ]]
  });
});
</script>

