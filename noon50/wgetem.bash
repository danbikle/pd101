#!/bin/bash

# /home/ann/pd101/noon50/wgetem.bash

mkdir -p /tmp/noon50/
cd       /tmp/noon50/

TKRH='%5EGSPC'
TKR='GSPC'
rm -f ${TKR}.html

wget --output-document=${TKR}.html  http://finance.yahoo.com/q?s=$TKRH

for TKR in GLD TLT FXI EFA XOM IWM EEM MDY EWJ
do
  echo $TKR
  rm -f ${TKR}.html
  wget --output-document=${TKR}.html http://finance.yahoo.com/q?s=$TKR
done
