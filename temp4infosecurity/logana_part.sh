#! /usr/bin/env bash

reportdate=$(date +%Y%m%d)
reporttime=$(date +%H%M%S)

cd /var/log/httpd
cat /var/log/httpd/access_log* | awk '{ print $4"-0000]\t"$1"\t"$9"\t"$11">><<"$7 }' | sed 's/\"//g' | sort > ~/httpdaccess$reportdate$reporttime.log
# ...
# cd ...
# tar zcvf httpdaccess.log.tgz httpdaccess$reportdate$reporttime.log
# ...

