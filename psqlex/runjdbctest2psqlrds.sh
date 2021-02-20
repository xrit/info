#! /usr/bin/env bash

if [ "$1" == "" ]
then
        echo "usage: $0 <test class/jdbc jar dir>"
        exit 0
fi
cd $1
java -cp .:postgresql-9.3-1102.jdbc41.jar jdbctest2psqlrds
