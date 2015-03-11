#!/bin/bash

# ~ann/pd101/pd101.bash

# This script should download data from Yahoo and then it should help me collect predictions.

cd ~ann/pd101/data/

export TKRH='%5EGSPC'

export TKR='GSPC'
rm -f ${TKR}.csv
wget --output-document=${TKR}.csv  http://ichart.finance.yahoo.com/table.csv?s=${TKRH}

cat ${TKR}.csv | awk -F, '{print $1 "," $5}' > ${TKR}2.csv
# I should use python to generate some features:
python ~ann/pd101/pd101.py     ${TKR}2.csv
grep -v cdate ftr${TKR}2.csv > ${TKR}3.csv

# I should use a for-loop to download more tkrs

for TKR in GLD TLT FXI EFA XOM IWM EEM MDY EWJ
do
  echo $TKR
  rm -f ${TKR}.csv
  wget --output-document=${TKR}.csv  http://ichart.finance.yahoo.com/table.csv?s=${TKR}
  cat ${TKR}.csv | awk -F, '{print $1 "," $5}' > ${TKR}2.csv
  # I should use python to generate some features:
  python ~ann/pd101/pd101.py     ${TKR}2.csv
  grep -v cdate ftr${TKR}2.csv > ${TKR}3.csv
done

# Now I should have new CSV files in ~ann/pd101/data/

set -x
# I should create wide1.csv
cd ~ann/pd101/
sqlite3 pd101.db '.read joinem.sql'

# I should backtest:
python bt10.py

exit
