<?php
$user = 'xyz?????';
$pass = '!!!abc003';
$dbh = new PDO('mysql:host=xdb?.xxxxxxxxxxxx.us-west-1.rds.amazonaws.com;dbname=xxxxxx', $user, $pass);
/* http://php.net/manual/en/pdostatement.bindparam.php */
/* Execute a prepared statement by binding PHP var */
$userid = 3;
$sth = $dbh->prepare('SELECT c1, c2, c3 
    FROM t2   
    WHERE c4 = :userid ');
$sth->bindParam(':userid', $userid, PDO::PARAM_INT);
$sth->execute();
$result = $sth->fetchAll();
echo "<pre>\n";
print_r($result);
echo "doing update ...\n";
$sth = $dbh->prepare('UPDATE t2   
    SET c2 = unix_timestamp(), c3 = utc_timestamp() 
    WHERE c4 = :userid ');
$sth->bindParam(':userid', $userid, PDO::PARAM_INT);
$sth->execute();
$sth = $dbh->prepare("SELECT * FROM t2 WHERE c1 = :iname");
$sth->bindParam(':iname', $iname);
$iname = 'xxx';
$sth->execute();
$result = $sth->fetchAll();
print_r($result);
echo "</pre>\n";
?>
