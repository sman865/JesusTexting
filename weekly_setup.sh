#!/bin/bash
# I suggest to run this every Sunday night: 
#     0 20 * * Sun
#
# Example output:
#
# Sun 4
# Mon 2
# ...
# Sat 6

days=("Sun" "Mon" "Tue" "Wed" "Thu" "Fri" "Sat")
nums=("0" "1" "2" "3" "4" "5" "6")
not_done=1

# shuffle array. it's an okay method of shuffling. shrug. O(n)...
for i in {0..6}; do
    rand=$((RANDOM%7))
    tmp=${nums[$i]}
    nums[$i]=${nums[$rand]}
    nums[$rand]=$tmp
done

for i in {0..6}; do
    echo ${days[$i]} ${nums[$i]}
done
