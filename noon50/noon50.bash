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

# I should cat them together
for TKR in GLD TLT FXI EFA XOM IWM EEM MDY EWJ GSPC
do
  cat ${TKR}recent.csv ${TKR}2.csv | grep -v Date > ${TKR}3.csv
done

exit
