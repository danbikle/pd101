# /home/ann/pd101/noon50/extprice.py

# This script should extract recent prices from html

import bs4
soup = bs4.BeautifulSoup(open("/tmp/noon50/GSPC.html"))
