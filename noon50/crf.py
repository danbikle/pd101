# /home/ann/pd101/noon50/crf.py
# This script should create features

# Demo:

# mkdir -p /tmp/noon50/
# cd       /tmp/noon50/
# export TKRH='%5EGSPC'
# export TKR='GSPC'
# rm -f ${TKR}.csv
# wget --output-document=${TKR}.csv  http://ichart.finance.yahoo.com/table.csv?s=${TKRH}
# cat ${TKR}.csv | awk -F, '{print $1 "," $5}' > ${TKR}2.csv
# python ~ann/pd101/noon50/crf.py ${TKR}2.csv

# I should check cmd line arg
import sys

print('hello, from '+ sys.argv[0])

