#! /usr/bin/bash

SQL_EX="psql"
USERID="postgres"
HOSTID="localhost"
PORTID="5432"
SCHEMA="idb"

echo "Connecting to $SQL_EX $SCHEMA with $USERID ..."
$SQL_EX postgresql://$HOSTID:$PORTID/$SCHEMA --username=$USERID --password 
