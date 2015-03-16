# ~ann/pd101/bt11.py

# This script should help me run backtests on this file:
# ~ann/pd101/data/wide1.csv

# Demo:
# cd ~ann/pd101/
# python bt11.py

import pdb
import pandas as pd
import numpy  as np
import sys

df1 = pd.read_csv('data/wide1.csv')

# How many observations have I?
obs_count = len(df1)
print('I have this many observations: '+str(obs_count))

# I should get this many predictions:
pcount = 10 # Near the max

# I should learn from this many observations:
train_count = 252 * 6

if pcount + train_count > obs_count:
  print('You need to lower pcount and-or train_count.')
  sys.exit()
  
# I should have this number of days between training data and oos data:
train_oos_gap = 0

# I should get some training data from df1.
# I should put it in NumPy Arrays.

number_of_rows    = len(df1)
number_of_columns = len(df1.columns)

# I should declare some integers to help me navigate the Arrays.
# The layout and names of the columns are specified by joinem.sql:

cdate_i   = 0
cp_i      = 1
pctlead_i = 2
dow_i     = 3
dom_i     = 4
moy_i     = 5
eem4_i    = 6

# I should use plain integers for the remaining 40 columns.

wide_a = np.array(df1)
x_a    = wide_a[:,eem4_i:  ]
y_a    = wide_a[:,pctlead_i]

# Ref:

# http://scikit-learn.org/stable/modules/ensemble.html#regression
# http://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html

from sklearn.ensemble  import GradientBoostingRegressor
from sklearn.neighbors import KNeighborsClassifier
model1 = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, max_depth=5, random_state=0, loss='ls')
model2 = KNeighborsClassifier(n_neighbors=(int(train_count)), weights='distance')

# I should use a list to save my predictions
model1_predictions_l = []
model2_predictions_l = []

# I should build a loop from pcount

for oos_i in range(0,pcount):
  print('Busy with prediction calculation: '+str(oos_i+1))
  x_oos       = x_a[oos_i,:]
  train_start = oos_i+1+train_oos_gap
  train_end   = train_start + train_count
  x_train     = x_a[train_start:train_end]
  y_train     = y_a[train_start:train_end]
  # yc_train  = y_train > 0
  yc_train    = y_train > np.mean(y_train)

  pdate   = wide_a[oos_i,cdate_i]
  model1.fit(x_train, y_train)
  model2.fit(x_train, yc_train)
  m1p     = model1.predict(x_oos)[0]
  m2p     = model2.predict_proba(x_oos)[0,1]
  pctlead = wide_a[oos_i,pctlead_i]
  model1_predictions_l.append([pdate, m1p, pctlead])
  model2_predictions_l.append([pdate, m2p, pctlead])

# I should try to use Pandas, avoid 0th prediction
backtest1_l = model1_predictions_l[1:]
backtest2_l = model2_predictions_l[1:]

prdf1 = pd.DataFrame(backtest1_l)
prdf2 = pd.DataFrame(backtest2_l)
prdf1.columns = ['cdate','prediction','actual']
prdf2.columns = ['cdate','prediction','actual']

# I should save my work
prdf1.to_csv('data/prdf1.csv', float_format='%4.3f', index=False)
prdf2.to_csv('data/prdf2.csv', float_format='%4.3f', index=False)
print('I have saved predictions in data/prdf1.csv now')
print('I have saved predictions in data/prdf2.csv now')

# I should get some predicates
pospp1 = prdf1['prediction'] >  0
pospp2 = prdf2['prediction'] >  0.5
negpp1 = prdf1['prediction'] <= 0
negpp2 = prdf2['prediction'] <= 0.5
posap1 = prdf1['actual']     >  0
posap2 = prdf2['actual']     >  np.mean(prdf1['actual'])
negap1 = prdf1['actual']     <= 0
negap2 = prdf2['actual']     <= np.mean(prdf1['actual'])

# I should apply predicates
# to get pos or neg predictions:
prposDF1 = prdf1[pospp1]
prposDF2 = prdf2[pospp2]
prnegDF1 = prdf1[negpp1]
prnegDF2 = prdf2[negpp2]

# I should get true positives/negatives
tpDF1 = prposDF1[posap1]
tpDF2 = prposDF2[posap2]
tnDF1 = prnegDF1[negap1]
tnDF2 = prnegDF2[negap2]

# I should get accuracy:
# 100 * (true-pos+true-neg)/total-predictions
acc1 = 100.0 * (len(tpDF1)+len(tnDF1)) / len(prdf1)
acc2 = 100.0 * (len(tpDF2)+len(tnDF2)) / len(prdf2)

# I should get effectiveness.
# For example:
# np.mean of prdf1 where prdf1['prediction'] < 0
# np.mean of prdf1 
# np.mean of prdf1 where prdf1['prediction'] > 0

effneg1 = np.mean(prdf1['actual'][negpp1])
effneg2 = np.mean(prdf2['actual'][negpp2])
mean1   = np.mean(prdf1['actual'])
# mean1 should == mean2
mean2   = np.mean(prdf2['actual'])
effpos1 = np.mean(prdf1['actual'][pospp1])
effpos2 = np.mean(prdf2['actual'][pospp2])

# My model1 is effective if effneg1 < mean1 < effpos1

# I should report:
print('Model1 Accuracy: '+str(acc1))
print('Model2 Accuracy: '+str(acc2))

# Effectiveness:

print('Model1 Mean-Gain-Bearish-Predictions: '+str(effneg1))
print('Model2 Mean-Gain-Below-Avg-Predictions: '+str(effneg2))

print('Long-Only Mean-Gain: '+str(mean1))

print('Model1 Mean-Gain-Bullish-Predictions: '+str(effpos1))
print('Model2 Mean-Gain-Above-Avg-Predictions: '+str(effpos2))

print('Prediction-Count: '+str(len(backtest1_l)))

print('Model1 Bearish-Prediction-Count: '+str(len(prnegDF1)))
print('Model2 Below-Avg-Prediction-Count: '+str(len(prnegDF2)))

print('Model1 Bullish-Prediction-Count: '+str(len(prposDF1)))
print('Model2 Above-Avg-Prediction-Count: '+str(len(prposDF2)))

'bye'

