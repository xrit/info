#! /usr/bin/env python

import sys

def isint(s):
  try:
    print ("%s is an integer !" % int(s))
    return True
  except ValueError:
    print ("%s is not an integer !" % s)
    return False

if (len(sys.argv) == 2):
  print (isint(sys.argv[1]))
else:
  print ("usage: sys.argv[0] <argument>")

