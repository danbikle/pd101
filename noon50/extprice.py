# /home/ann/pd101/noon50/extprice.py

# This script should extract recent prices from html

import bs4
import datetime
import pdb

soup   = bs4.BeautifulSoup(open("/tmp/noon50/GSPC.html"))
span0  = soup.find(id="yfs_market_time")
date_l = span0.string.split(",")[:3]
date_s = date_l[1]+date_l[2]
mydt   = datetime.datetime.strptime(date_s, " %b %d %Y")
mydt_s = mydt.strftime('%Y-%m-%d')

span1 = soup.find(id="yfs_l10_^gspc")
pdb.set_trace()
gspc_price = span1.string.replace(',','')
gspc_s = mydt_s+','+gspc_price+"\n"
gspcf = open('recent_gspc.csv','w')
gspcf.write(gspc_s)
gspcf.close()



