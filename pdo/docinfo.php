<?php

echo "<html><head>\n";
echo "<meta http-equiv=Content-Type content=text/html; charset=utf-8>\n";
echo "</head>\n";
echo "<body>\n";
echo "Trying to make php/mysql database connection ...<br />\n";
// Connecting, selecting database
$link = mysql_connect('scratchdba.db.5534620.hostedresource.com', 'scratchdba', 'phpMySQL5')
    or die('Could not connect: ' . mysql_error());
echo 'Connected successfully';
mysql_select_db('scratchdba') or die('Could not select database');

// Performing SQL query
$query = 'SELECT now()';
$result = mysql_query($query) or die('Query failed: ' . mysql_error());

// Printing results in HTML
echo "<h3><table>\n";
while ($line = mysql_fetch_array($result, MYSQL_ASSOC)) {
    echo "\t<tr>\n";
    foreach ($line as $col_value) {
        echo "\t\t<td><b>$col_value</b></td>\n";
    }
    echo "\t</tr>\n";
}
echo "</table></h3>\n";

// Performing SQL query
$query = 'SELECT * FROM contactinfo ORDER BY TimeID DESC';
$result = mysql_query($query) or die('Query failed: ' . mysql_error());

// Printing results in HTML
echo "<table>\n";
while ($line = mysql_fetch_array($result, MYSQL_ASSOC)) {
    echo "\t<tr>\n";
    foreach ($line as $col_value) {
        echo "\t\t<td>$col_value</td>\n";
    }
    echo "\t</tr>\n";
}
echo "</table>\n";

// Free resultset
mysql_free_result($result);

// Closing connection
mysql_close($link);

echo "</body></html>\n";

?>