#!/bin/bash

# ~ann/pd101/noon50/noon50.bash

# This script should help me predict the next one day pctgain for GSPC.
# I should run this script at 12:50 pm California time.

if [ -e ~ann/pd101/noon50/ ]; then
  echo $0 is in the correct folder.
else
  echo $0 needs to reside here:
  echo ~ann/pd101/noon50/
  echo bye.
  exit 1
fi

mkdir -p /tmp/noon50/
cd       /tmp/noon50/

# I should get both csv and html data
echo ~ann/pd101/noon50/wgetem.bash

# I should extract recent prices from html
echo python ~ann/pd101/noon50/extprice.py

# I should cat them together and generate features
for TKR in GLD TLT FXI EFA XOM IWM EEM MDY EWJ GSPC
do
  echo cdate,cp                                   >  ${TKR}3.csv
  cat ${TKR}recent.csv ${TKR}2.csv | grep -v Date >> ${TKR}3.csv
  python ~ann/pd101/noon50/genf.py                   ${TKR}3.csv
  grep -v cdate ftr${TKR}3.csv > ${TKR}4.csv
done
exit

# I should create wide1.csv
sqlite3 noon50.db '.read ~ann/pd101/noon50/joinem.sql'

exit
