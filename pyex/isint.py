#! /usr/bin/env python

import sys

def isint(s):
  try:
    print int(s), "is an integer !"
    return True
  except ValueError:
    return False

if (len(sys.argv) == 2):
  print isint(sys.argv[1])
