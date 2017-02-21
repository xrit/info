#! /usr/bin/env python

import distanceFunc
import mysql.connector

execfile("../dbcred.py")

totaldist = -1
cnx = mysql.connector.connect(user=username, password=passcode, host=hostname, database=dataname)
idate = raw_input('UTC Date (YYYY-MM-DD) ? ')
...
    dist = distanceFunc.calculate_distance_in_km(lati0, long0, lati1, long1)
    totaldist = totaldist + dist
    print dt_ms, "\t", dtime, "\t", 
    print '{:+10.9f}'.format(lati0), "\t", '{:+10.9f}'.format(long0), "\t", 
    print '{:+10.9f}'.format(lati1), "\t", '{:+10.9f}'.format(long1), "\t", 
    print '{:20.9f}'.format(dist), "\t", totaldist
...
