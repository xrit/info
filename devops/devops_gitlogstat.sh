#! /usr/bin/env bash

if [ "$1" == "" ] || [ "$2" == "" ] || [ "$3" == "" ]
then
  echo "usage: $0 <from YYYY-MM-DD> <to YYYY-MM-DD> <repo dir>"
  exit 0
fi

from=$1
to=$2
gitdir=$3

cd $gitdir

git log --after="$from 00:00:00" --before="$to 00:00:00" --stat

