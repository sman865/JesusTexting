#!/bin/bash
# I suggest to run this every day:
#     0 6 * * *
#
# This is a minor script to call the main python program.

cd /home/pi/git/JesusTexting/
day=$(date +%a)
arg=$(awk "/$day/ {print \$2}" current_order)
./JesusTexting.py $arg 2>>error_log.txt
