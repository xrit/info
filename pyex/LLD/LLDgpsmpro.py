#! /usr/bin/env python

import distanceFunc
import mysql.connector

execfile("../dbcred.py")

totaldist = -1
cnx = mysql.connector.connect(user=username, password=passcode, host=hostname, database=dataname)
idate = raw_input('UTC Date (YYYY-MM-DD) ? ')

...


