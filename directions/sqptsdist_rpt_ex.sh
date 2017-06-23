#! /usr/bin/env bash

mysql -p -h127.0.0.1 < sqptsdist_rpt.mysql

echo
echo
echo "Report Date/Time:"
date
echo
echo "Copyright (C) 2017 http://admylocation.com/ " 
