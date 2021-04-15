#! /usr/bin/env python

import datetime
import sys

if (len(sys.argv) != 2):
   print("\n   Usage:   %s  <YYYY-MM-DD> \n" % sys.argv[0])
   sys.exit(0)

str_date = sys.argv[1]
str_format = '%Y-%m-%d'

istrd = datetime.datetime.strptime(str_date, str_format)
nextd = istrd + datetime.timedelta(days=1)
prevd = istrd + datetime.timedelta(days=-1)

print(prevd)
print(istrd)
print(nextd)

