# /home/ann/pd101/noon50/extprice.py

# This script should extract recent prices from html

import pdb
import bs4
soup = bs4.BeautifulSoup(open("/tmp/noon50/GSPC.html"))

span1 = soup.find(id="yfs_l10_^gspc")
pdb.set_trace()
gspc_price = span1.string.replace(',','')

