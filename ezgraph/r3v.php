<html>
<head>
<title>3v</title>
</head>
<body>
<script type="text/javascript" src="./lib/dygraph-combined.js"></script>

<div id="graph" style="width:100%;height:100%;"></div>

<script type="text/javascript">
  new Dygraph( document.getElementById("graph"),
    "./data/3v.csv",
    {
    'title': '3V X',
    'showRangeSelector': true,
    'maxNumberWidth': 30,
    'rollPeriod': 1,
    'showRoller': true
    }
  );
</script>
</body>
</html>
<?php
require '../log2db/rdsmysql.php';
logdb('samplexgraph/r3v.php');
?>
