#! /usr/bin/env python

import sqlite3

conn = sqlite3.connect('ex2')
c = conn.cursor()

# Create table
c.execute('''CREATE TABLE IF NOT EXISTS tst
             (date text, trans text, info text, qty real, price real)''')

# Delete 
c.execute("DELETE FROM tst")

# Insert a row of data
c.execute("INSERT INTO tst VALUES ('2012-10-05','BUY','TIX',100,20.00)")

# Commit
conn.commit()

# Close the connection after commit().
conn.close()

# More testing ...
conn = sqlite3.connect('ex2')
c = conn.cursor()

t = ('TIX',)
c.execute('SELECT * FROM tst WHERE info=?', t)
print c.fetchone()

print "=== t1 ==="

# Insert 2 rows of data
c.execute("INSERT INTO tst VALUES ('2014-10-05','BUY','TIX',300,30.00)")
c.execute("INSERT INTO tst VALUES ('2016-10-05','BUY','TIX',200,50.00)")

# Commit
conn.commit()

# Select
for row in c.execute('SELECT * FROM tst WHERE info=?', t):
   print row

print "=== t2 ==="

# Update
u = (40,'TIX','2012-10-05')
c.execute("UPDATE tst SET price=? WHERE info=? AND date=?", u)
for row in c.execute('SELECT * FROM tst WHERE info=?', t):
   print row
 
print "=== t3 ==="

# Inserts many records at a time
purchases = [('2012-03-28', 'BUY', 'PIX', 1000, 40.00),
             ('2013-09-20', 'BUY', 'STY', 1000, 12.00),
             ('2013-01-06', 'SELL', 'PIX', 500, 50.00),
            ]
c.executemany('INSERT INTO tst VALUES (?,?,?,?,?)', purchases)

# Commit
conn.commit()

# Execute query and print the data
for r in c.execute('SELECT * FROM tst ORDER BY date, info'):
   print r[0], '\t', r[2], '\t', r[1], '\t', r[4], '\t', r[3] 

# Close connection before exit
conn.close()


