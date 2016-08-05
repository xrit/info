var pg = require('pg');
 
var conString = "postgres://psqluser:psqlpasscode@localhost/rdb";
 
var client = new pg.Client(conString);

var queryString = "SELECT SUBSTRING(ts FROM 4 FOR 20) AS \"theTime\", lat_info, long_info, ipaddress FROM pgtable WHERE SUBSTRING(ts FROM 1 FOR 3) IN ('xxx','yyy','zzz') ORDER BY 1 DESC";

client.connect(function(err) {
  if(err) {
    return console.error('could not connect to postgres', err);
  }
  client.query(queryString, function(err, result) {
    if(err) {
      return console.error('error running query', err);
    }
    for (i = 0; i < 30; i++) {
       console.log(result.rows[i].theTime, '\t', result.rows[i].lat_info, '\t', result.rows[i].long_info, '\t', result.rows[i].ipaddress);
    }
    client.end();
  });
});
