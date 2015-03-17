#!/bin/bash

# /home/ann/pd101/noon50/wgetem.bash

mkdir -p /tmp/noon50/
cd       /tmp/noon50/

TKRH='%5EGSPC'
TKR='GSPC'
rm -f ${TKR}.html ${TKR}.csv

wget --output-document=${TKR}.html http://finance.yahoo.com/q?s=$TKRH
wget --output-document=${TKR}.csv  http://ichart.finance.yahoo.com/table.csv?s=${TKRH}
cat ${TKR}.csv | awk -F, '{print $1 "," $5}' > ${TKR}2.csv

for TKR in GLD TLT FXI EFA XOM IWM EEM MDY EWJ
do
  echo $TKR
  rm -f ${TKR}.html ${TKR}.csv
  wget --output-document=${TKR}.html http://finance.yahoo.com/q?s=$TKR
  wget --output-document=${TKR}.csv  http://ichart.finance.yahoo.com/table.csv?s=${TKR}
  cat ${TKR}.csv | awk -F, '{print $1 "," $5}' > ${TKR}2.csv
done
