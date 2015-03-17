#!/bin/bash

# /home/ann/pd101/noon50/noon50.bash

# This script should help me predict the next one day pctgain for GSPC.
# I should run this script at 12:50 pm California time.

if [ -e /home/ann/pd101/noon50/ ]; then
  echo $0 is in the correct folder.
else
  echo $0 needs to reside here:
  echo /home/ann/pd101/noon50/
  echo bye.
  exit 1
fi

mkdir -p /tmp/noon50/
cd       /tmp/noon50/

export TKRH='%5EGSPC'

export TKR='GSPC'
rm -f ${TKR}.csv
wget --output-document=${TKR}.csv  http://ichart.finance.yahoo.com/table.csv?s=${TKRH}

cat ${TKR}.csv | awk -F, '{print $1 "," $5}' > ${TKR}2.csv
# I should use python to generate some features:
python ~ann/pd101/noon50/crf.py     ${TKR}2.csv
exit

grep -v cdate ftr${TKR}2.csv > ${TKR}3.csv




# I should use a for-loop to download more tkrs

for TKR in GLD TLT FXI EFA XOM IWM EEM MDY EWJ
do
  echo $TKR
  rm -f ${TKR}.csv
  wget --output-document=${TKR}.csv  http://ichart.finance.yahoo.com/table.csv?s=${TKR}
  cat ${TKR}.csv | awk -F, '{print $1 "," $5}' > ${TKR}2.csv
  # I should use python to generate some features:
  python ~ann/pd101/noon50/crf.py     ${TKR}2.csv
  grep -v cdate ftr${TKR}2.csv > ${TKR}3.csv
done

# Now I should have new CSV files in ~ann/pd101/data/

set -x
# I should create wide1.csv
cd ~ann/pd101/
sqlite3 pd101.db '.read joinem.sql'

