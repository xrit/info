#! /usr/bin/env bash

date
uname -a
mysql -uroot -hlocalhost -p -e "select now(), utc_timestamp();show full processlist" 

