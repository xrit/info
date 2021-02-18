#! /usr/bin/env python

import sys

def isfloat(s):
  try:
    print ("%f is a floating point number!" % float(s))
    return True
  except ValueError:
    print ("%s is not a floating point number!" % s)
    return False

if (len(sys.argv) == 2):
  print (isfloat(sys.argv[1]))
else:
  print ("usage: %s <argument>" % sys.argv[0])

