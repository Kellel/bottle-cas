#!/bin/sh

# Shell script to clean up defualt beaker directory
# Copy this script to /root and install in CRON with the quoted string on the
# next line
# "0 2 * * * /root/cleanup.sh &> /dev/null"

BEAKER_DATA_DIR=/tmp/beaker/data
BEAKER_LOCK_DIR=/tmp/beaker/lock

find $BEAKER_DATA_DIR -mmin +60 -delete
find $BEAKER_DATA_DIR -type d -empty -delete
find $BEAKER_LOCK_DIR -mmin +60 -delete
find $BEAKER_LOCK_DIR -type d -empty -delete

