#! /usr/bin/env bash

~/logana/brief_access_log.sh | grep -v "Exec Date/Time" | awk '{ print "status: " $3 "\t\tdate/time: " $2 "\t\tipaddress: " $1}'

