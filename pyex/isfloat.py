#! /usr/bin/env python

import sys

def isfloat(s):
  try:
    print float(s), "is a floating point number!"
    return True
  except ValueError:
    return False

if (len(sys.argv) == 2):
  print isfloat(sys.argv[1])
