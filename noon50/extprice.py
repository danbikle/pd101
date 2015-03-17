# /home/ann/pd101/noon50/extprice.py

# This script should extract recent date, prices from html

import bs4
import datetime
import pdb

soup   = bs4.BeautifulSoup(open("/tmp/noon50/GSPC.html"))
span0  = soup.find(id="yfs_market_time")
date_l = span0.string.split(",")[:3]
date_s = date_l[1]+date_l[2]
mydt   = datetime.datetime.strptime(date_s, " %b %d %Y")
mydt_s = mydt.strftime('%Y-%m-%d')

print('GSPC')
# GSPC needs special handling here:
span1      = soup.find(id="yfs_l10_^gspc")

gspc_price = span1.string.replace(',','')
gspc_s     = mydt_s+','+gspc_price+"\n"
gspcf      = open('GSPCrecent.csv','w')
gspcf.write(gspc_s)
gspcf.close()

# I should use a loop on the other tkrs
for tkr in ['GLD','TLT','FXI','EFA','XOM','IWM','EEM','MDY','EWJ']:
  print(tkr)
  ltkr = tkr.lower()
  soup   = bs4.BeautifulSoup(open("/tmp/noon50/"+tkr+".html"))
  span1     = soup.find(id="yfs_l84_"+ltkr)
  tkr_price = span1.string.replace(',','')
  tkr_s     = mydt_s+','+tkr_price+"\n"
  tkrf      = open(tkr+'recent.csv','w')
  tkrf.write(tkr_s)
  tkrf.close()
