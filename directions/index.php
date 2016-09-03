<html>
<head>
<title>DirectRequestor</title>
</head>
<body>
<?php

$dir = $_GET['vpx'];

switch ($dir) {
  case 'locinfo':
    $urq = 'http://www.admylocation.info';
    break;
  case 'contact':
    $urq = 'http://contact.advisical.com';
    break;
  case 'homeart':
    $urq = 'http://admylocation.com/homeart';
    break;
  case 'xyz':
    $urq = 'http://www.admylocation.xyz';
    break;
  default:
    $urq = 'http://www.advisical.com';
}

echo "<script language='JavaScript'>";
echo "document.location.href = '" . $urq . "'";
echo "</script>";

?>
</body>
</html>
