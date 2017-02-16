#! /usr/bin/env python
#
# MySQL DML for Python   
#

import datetime
import mysql.connector


execfile('dbcred.py')

def select_table (arg):
  query = "select * from %s " % arg
  print query
  cnx = mysql.connector.connect(user=username, password=passcode, host=hostname, database=dataname)
  tcursor = cnx.cursor()
  tcursor.execute(query)
  for row in tcursor:
    for col in row:
      print col,
    print
  tcursor.close()
  cnx.close()


