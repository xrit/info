#! /usr/bin/env bash

if [ "$1" == "" ] || [ "$2" == "" ] || [ "$3" == "" ] 
then
	echo "usage: $0 <user> <host> <database>"
	exit 0
fi

mysql -u$1 -h$2 $3 -p < selectfromcitiesexample.mysql

