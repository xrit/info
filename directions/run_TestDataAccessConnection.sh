#! /usr/bin/env bash

# JDBC Driver Path: ~/jdbcdrivers/mysql-connector-java-5.1.10-bin.jar

# TestDataAccessConnection and DataAccessConnection are compiled on my local machine.

export JDBCJARCLASSPATH=~/jdbcdrivers/mysql-connector-java-5.1.10-bin.jar

java -cp .:$JDBCJARCLASSPATH TestDataAccessConnection 
