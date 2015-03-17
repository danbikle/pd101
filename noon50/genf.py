# ~ann/pd101/noon50/genf.py
# This script should generate features

# Demo:
# cd /tmp/noon50/
# python ~ann/pd101/noon50/genf.py EEM3.csv

# I should check cmd line arg
import sys

print('hello, from '+ sys.argv[0])

import pandas as pd
import numpy  as np
import pdb
# I should check cmd line arg

#  len(sys.argv) should == 2
if len(sys.argv) == 1:
  print('Demo:')
  print('cd /tmp/noon50/')
  print('python ~ann/pd101/noon50/genf.py GSPC3.csv')
  print('...')
  sys.exit()

print(sys.argv[1])

df1 = pd.read_csv(sys.argv[1])
df1.columns = ['cdate','cp']
pdb.set_trace()
df1.head()
