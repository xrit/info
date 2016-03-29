#! /usr/bin/env bash

reportdate=$(date +%Y%m%d)
reporttime=$(date +%H%M%S)

pg_dump postgresql://localhost:5432/idb --username=postgres --password > idb$reportdate$reporttime.backup.psql
 

