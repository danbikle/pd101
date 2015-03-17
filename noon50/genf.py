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
  print('python ~ann/pd101/noon50/genf.py EEM3.csv')
  print('...')
  sys.exit()

print(sys.argv[1])

df1  = pd.read_csv(sys.argv[1])
cp_a = df1[['cp']].values
cp   = [elm[0] for elm in cp_a]

cplead = [cp[0]] + cp
cplag1 = cp +     [cp[-1]]
cplag2 = cp +     [cp[-1]] + [cp[-1]]
cplag4 = cp +     [cp[-1]] + [cp[-1]] + [cp[-1]] + [cp[-1]]
cplag8 = cplag4 + [cp[-1]] + [cp[-1]] + [cp[-1]] + [cp[-1]]
# I should snip off ends so new columns as long as cp:
cplead = cplead[:-1]
cplag1 = cplag1[1:]
cplag2 = cplag2[2:]
cplag4 = cplag4[4:]
cplag8 = cplag8[8:]
# I should check new columns as long as cp:
len(cp) == len(cplead)
len(cp) == len(cplag4)

# NumPy allows me to do arithmetic on its Arrays.
# I should convert my lists to Arrays:
cp_a     = np.array(cp)
cplead_a = np.array(cplead)
cplag1_a = np.array(cplag1)
cplag2_a = np.array(cplag2)
cplag4_a = np.array(cplag4)
cplag8_a = np.array(cplag8)

# I should calculate pct-deltas:
pctlead_a = 100.0 * (cplead_a - cp_a)/cp_a
pctlag1_a = 100.0 * (cp_a - cplag1_a)/cplag1_a
pctlag2_a = 100.0 * (cp_a - cplag2_a)/cplag2_a
pctlag4_a = 100.0 * (cp_a - cplag4_a)/cplag4_a
pctlag8_a = 100.0 * (cp_a - cplag8_a)/cplag8_a

# I am done doing calculations.
# I should put my 5 new columns into my DataFrame.

df1['pctlead'] = pctlead_a
df1['pctlag1'] = pctlag1_a
df1['pctlag2'] = pctlag2_a
df1['pctlag4'] = pctlag4_a
df1['pctlag8'] = pctlag8_a

# I should save my work into a CSV file.
# My input file should look something like this:
# EEM3.csv
# I should save my work as something like this:
# ftrEEM3.csv
df1.to_csv('ftr'+sys.argv[1], float_format='%4.3f', index=False)

# done
