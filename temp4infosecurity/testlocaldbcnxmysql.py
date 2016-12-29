#! /usr/bin/env python

import localdbcnx
import mysql.connector
import sys 

if (len(sys.argv) <> 2):
  print sys.argv[0], "<database schema>"
  exit()
dbx = sys.argv[1]
cnx = localdbcnx.open(dbx)
cur = cnx.cursor()
qry = "select print_id, artist_id, image_name from prints order by print_id"
cur.execute(qry)
for row in cur:
  for col in row:
    print col, "\t",
  print
cur.close()
cnx.close()

