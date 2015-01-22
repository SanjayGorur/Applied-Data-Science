##############################################
##############################################
#      Applied Data Science GX5004           # 
#      Assignment 2                          #
#      Dimas Rinarso Putro | drp354@nyu.edu  #
#      No.1g                                 #
##############################################

import argparse,csv,sys,os
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
from pandas.tools.plotting import scatter_matrix as scatter
from pandas.io.stata import read_stata as rd_stata
import statsmodels.api as sm
from statsmodels.sandbox.regression.predstd import wls_prediction_std

#Read data
filename = 'griliches.dta'
df = rd_stata(filename)
df['a'] = pd.Series((df['age']*df['age']), index=df.index)
x = []

#===========Least square regression
#=====================
#lw VS multivariates 
#=====================
#plot the linear regression
#and also the confidence level
#============print the summary for each column
x= df[['rns','mrt','smsa','med','iq','kww','age','s','expr','a']]
y = df.lw
X = sm.add_constant(x)
model = sm.OLS(y, X)
results = model.fit()
print(results.summary())


plt.figure();
plt.plot(x, y, 'o');
prstd, iv_l, iv_u = wls_prediction_std(results)
plt.plot(x, results.fittedvalues, 'g--.')
#plt.plot(x, iv_u, 'r--')
#plt.plot(x, iv_l, 'r--')
plt.xlabel('multivariates')
plt.ylabel('Log Wage')
plt.title('Multivariates');
plt.savefig('1-multivariates-1g.png')
#plt.show()

