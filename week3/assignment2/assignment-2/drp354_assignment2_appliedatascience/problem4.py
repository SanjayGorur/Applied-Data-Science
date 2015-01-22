##############################################
##############################################
#      Applied Data Science GX5004           # 
#      Assignment 2                          #
#      Dimas Rinarso Putro | drp354@nyu.edu  #
#      No.4                                  #
##############################################

import argparse,csv,sys,os
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
from pandas.tools.plotting import scatter_matrix as scatter
from pandas.io.stata import read_stata as rd_stata
import statsmodels.api as sm

###No.4###
##############################################
#Read data
filename = 'train.dta'
df = rd_stata(filename)

#print the summary for each column
print 'd='
print df['d'].describe()
print 'x1='
print df['x1'].describe()

#sorting
print df.head()
result =df.sort(['x1'], ascending=[1])

X = df.x1
y = df.d

#linear regression d on x1
X = sm.add_constant(X)
model = sm.OLS(y, X)
results = model.fit()
print(results.summary())

#plot sorted column into scatterplot
#for better understanding
plt.scatter(result['d'],result['x1'])
plt.xlabel('d')
plt.ylabel('x1')
plt.show()

