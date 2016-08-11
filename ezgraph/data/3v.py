#! /usr/bin/env python

def y(x):
  return x*x+9

def z(x):
  return 6*x+30

print "X\tY\tZ"
for x in range(20):
  print x, "\t", y(x), "\t", z(x) 
