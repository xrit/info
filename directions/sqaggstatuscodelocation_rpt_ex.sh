#! /usr/bin/env bash

if test $# == 0  # note: = -eq
then
  echo "Usage: $0 <db>"
else
  mysql -p -h127.0.0.1 $1 < aggregate_statuscode_yyyymmdd_location.qbquery
fi

echo
echo
echo "Report Date/Time:"
date
echo
echo "Copyright (C) 2017 http://admylocation.com/ " 
