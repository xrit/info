#! /usr/bin/env python

import sqlite3

conn = sqlite3.connect('ex')
c = conn.cursor()

# Create table
c.execute('''CREATE TABLE IF NOT EXISTS tst
             (date text, trans text, info text, qty real, price real)''')

# Insert a row of data
c.execute("INSERT INTO tst VALUES ('2012-10-05','BUY','TIX',100,35.00)")

# Commit
conn.commit()

# Close the connection after commit().
conn.close()

# More testing ...
conn = sqlite3.connect('ex')
c = conn.cursor()

t = ('TIX',)
c.execute('SELECT * FROM tst WHERE info=?', t)
print c.fetchone()

# Inserts many records at a time
purchases = [('2012-03-28', 'BUY', 'PIX', 1000, 40.00),
             ('2013-09-20', 'BUY', 'STORIES', 1000, 12.00),
             ('2013-01-06', 'SELL', 'PIX', 500, 50.00),
            ]
c.executemany('INSERT INTO tst VALUES (?,?,?,?,?)', purchases)

# Execute query and print the data
for row in c.execute('SELECT * FROM tst ORDER BY price'):
        print row

