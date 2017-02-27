#!/bin/sh

BEAKER_DATA_DIR=/tmp/beaker/data
BEAKER_LOCK_DIR=/tmp/beaker/lock

find $BEAKER_DATA_DIR -mmin +60 -delete
find $BEAKER_DATA_DIR -type d -empty -delete
find $BEAKER_LOCK_DIR -mmin +60 -delete
find $BEAKER_LOCK_DIR -type d -empty -delete

