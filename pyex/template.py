#! /usr/bin/env python

import sys

def func(argf):
  print(argf)
 
def main(): 
  if len(sys.argv) != 2:
    print("Usage: python " + sys.argv[0] + " <argument> ")
    exit()
  elif sys.argv[1] == '?':
    print("Please input an argument.")
    if sys.version_info[0] < 3:
      argument = raw_input('Argument? ')
    else:
      argument = input('Argument? ')
  else: 
    argument = sys.argv[1]
  for i in range(0,10):
    sys.stdout.write("Your argument: %s %d\n" % (argument, i))
  for t in list(argument):
    print(t)
  for s in range(3):
    func(argument)

if __name__ == '__main__':
  main()

