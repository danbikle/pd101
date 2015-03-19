#!/bin/bash

# /home/ann/pd101/plot/plotem.bash

# This script should plot data in a CSV file

# Demo:
# /home/ann/pd101/plot/plotem.bash /tmp/pd101/prdf1.csv

if [ $# -ne 1 ]
then
  echo I need 1 arg.
  echo Demo:
  echo $0 /tmp/pd101/prdf1.csv
  exit 1
fi

echo Working...

python /home/ann/pd101/plot/plotem.py $1

exit
