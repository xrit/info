#! /usr/bin/env bash
if [ "$1" == "" ]
then
	echo "usage: $0 <jdbc jar dir>"
	exit 0
fi
java -cp $1/mysql-connector-java-5.1.10-bin.jar:. jdbctest2mariadb_localhost
