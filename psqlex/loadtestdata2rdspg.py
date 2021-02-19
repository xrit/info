#! /usr/bin/env python

import datetime
import psycopg2
import sys
import time

if len(sys.argv) != 4:
    print "Usage: python " + sys.argv[0] + " <argument for # test rows> <rds endpoint> <passcode>"
    exit()
else:
  try:
     # convert to integer
     dl = int(sys.argv[1])
     arg_is_int = True
     endpt = sys.argv[2]
     pcode = sys.argv[3]
  except ValueError:
     arg_is_int = False
  if arg_is_int == False:
    print "Usage: python " + sys.argv[0] + " <argument for # test rows> <rds endpoint> <passcode>"
    exit()

## test psql
try:
    conn = psycopg2.connect("dbname='sitestat' user='postgres' host='%s' password='%s'" % (endpt,pcode))
except:
    print("I am unable to connect to the database")
    exit()

print("I am able to connect to postgres")

cur = conn.cursor()
cur.execute("""SELECT datname from pg_database""")
rows = cur.fetchall()
print("\nShow me the databases:\n")
for row in rows:
    print("   %s" % row[0])
cur.close()

## load data into sitestat's testdata table
print("\n")
print(datetime.datetime.now())
print("Loading data into testdata ...")
print("...")

cur2 = conn.cursor()
query = "drop table if exists testdata"
cur2.execute(query)
query = "create table testdata (id integer primary key, ts integer, info varchar(100), did integer)"
cur2.execute(query)
for i in range(0,dl):
   timex = time.time()
   t = int(timex)
   d = int((timex - t) * 1000000)
   query = "insert into testdata (id, ts, info, did) values (%d, %d, '%s', %d)" % (i, t, str(datetime.datetime.now()), d)
   cur2.execute(query)
conn.commit()
cur2.close()
conn.close()

print("Done loading data")
print(datetime.datetime.now())

### testdata query
# select now();
# select t2.*, t1.*, t2.did-t1.did from testdata t2 left join testdata t1 on (t2.id - 1 = t1.id) order by t2.id limit 10;


