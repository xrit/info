#! /usr/bin/env bash

case $# in
0) echo "$0 <time in ms>" ;;
1) java com.experimentalproj.T2D $1 ;;
*) echo "This shell script takes one argument only" ;;
esac

