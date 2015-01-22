##############################################
##############################################
#      Applied Data Science GX5004           # 
#      Assignment 3                          #
#      Dimas Rinarso Putro | drp354@nyu.edu  #
#      No.2a                                 #
##############################################

import argparse,csv,sys,os
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
from pandas.tools.plotting import scatter_matrix as scatter
from pandas.io.stata import read_stata as rd_stata
import statsmodels.api as sm
from statsmodels.sandbox.regression.predstd import wls_prediction_std

#variable initialization
mu, sigma = 0, 1
num_samples = 10000

#generate random numbers
x1 = np.random.normal(mu, sigma, num_samples)
x2 = np.random.normal(mu, sigma, num_samples)
e = np.random.normal(mu, sigma, num_samples)
y = 1+1*x1+1*x2+e

#estimate the b1 value
#plot the linear regression
X = sm.add_constant(x1)
model = sm.OLS(y, X)
results = model.fit()
print(results.summary())

#plot it
plt.figure();
plt.plot(x1, y, 'o');
prstd, iv_l, iv_u = wls_prediction_std(results)
plt.plot(x1, results.fittedvalues, 'g--.')
plt.xlabel('x1')
plt.ylabel('y')
plt.title('Finding b1')
plt.savefig('2a.png')
plt.show()
