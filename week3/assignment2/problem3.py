##############################################
##############################################
#      Applied Data Science GX5004           # 
#      Assignment 3                          #
#      Dimas Rinarso Putro | drp354@nyu.edu  #
##############################################

import argparse,csv,sys, os
import numpy as np
from matplotlib import pyplot as plt
import pylab 
from pandas.io.data import DataReader
import pandas as pd
from pandas.tools.plotting import scatter_matrix as scatter
from datetime import date,datetime
from matplotlib.dates import date2num
import statsmodels.api as sm

###No.3###
###########################################

#Read data
df_mic = DataReader('MSFT','yahoo',start='09/18/2004',end='09/18/2014')
df_nas = DataReader('^IXIC','yahoo',start='09/18/2004',end='09/18/2014')

#calculate log returns
df_mic['Return'] = np.log(df_mic['Close']/df_mic['Close'].shift(1))
df_nas['Return'] = np.log(df_nas['Close']/df_nas['Close'].shift(1))

#print to screen
print df_mic['Return'].describe() 
print df_nas['Return'].describe() 

#histogram of Microsoft stock
plt.figure();
df_mic['Return'].diff().hist()
plt.xlabel('Distribution')
plt.ylabel('Log Return MSFT')
plt.show()

#scatterplot of both log returns
df_mic['Return'].plot()
df_nas['Return'].plot(secondary_y=True, style='g')
plt.xlabel('distribution')
plt.ylabel('Log Return MSFT')
plt.show()

##calculate alpha
X=df_mic.Return[1:]
y=df_nas.Return[1:]
X = sm.add_constant(X)
model = sm.OLS(y, X)
results = model.fit()
print(results.summary())

#scatterplot of both log returns
plt.scatter(df_mic['Return'],df_nas['Return'])
plt.xlabel('Log Return MSFT')
plt.ylabel('Log Return Nasdaq')
plt.show()
