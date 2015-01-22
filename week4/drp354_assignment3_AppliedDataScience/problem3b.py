##############################################
##############################################
#      Applied Data Science GX5004           # 
#      Assignment 2                          #
#      Dimas Rinarso Putro | drp354@nyu.edu  #
#      No.1g                                 #
##############################################

import argparse,csv,sys,os
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from pandas.tools.plotting import scatter_matrix as scatter
from pandas.io.stata import read_stata as rd_stata
import statsmodels.api as sm
from statsmodels.sandbox.regression.predstd import wls_prediction_std

#Read data
filename = 'union.dta'
df = rd_stata(filename)
df_sliced = df[df['year'] >=70] 
df_sliced = df_sliced[df['year'] <=78] 

#===========Least square regression
#============print the summary for each column
#year  age  grade  south  union  black  smsa
x= df[['year','age','grade','south','black','smsa']]
y = df.union
X = sm.add_constant(x)
model_linear = sm.OLS(y, X)
results_linear = model_linear.fit()
print(results_linear.summary())

#===========Logit square regression
#============print the summary for each column
#year  age  grade  south  union  black  smsa
model_logit = sm.Logit(y, X)
results_logit = model_logit.fit()
print(results_logit.summary())
