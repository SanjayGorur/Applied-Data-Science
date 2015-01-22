##############################################
##############################################
#      Applied Data Science GX5004           # 
#      Assignment 3                          #
#      Dimas Rinarso Putro | drp354@nyu.edu  #
#      No.3c                                 #
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

#for creating model
df_sliced2 = df[df['year'] >=70] 
df_sliced = df_sliced2[df['year'] <=78] 

#for creating model
df_sample2 = df[df['year'] >=80] 
df_sample = df_sample2[df['year'] <=88] 

#===========get the data into parameters for model fit
x= df_sliced[['year','age','grade','south','black','smsa']]
y = df_sliced.union
X = sm.add_constant(x)
#===========Least square regression
model_linear = sm.OLS(y, X)
results_linear = model_linear.fit()
print(results_linear.summary())

#===========Logit square regression
results_logit = model_logit.fit()
print(results_logit.summary())

#===========y_hatimation
actual_linear = []
actual_logit = []
act_linear = []
act_logit = []
y_hat_linear = []
y_hat_logit = []
var= df_sample[['year','age','grade','south','black','smsa']]
X_pred = sm.add_constant(var)

##==================Predicted Value for 80-88
y_hat_linear = results_linear.predict(X_pred)
union_count_linear = 0
for people in y_hat_linear:
  if float(people) > 0.25: union_count_linear += 1
  else:pass
print '\n\nLINEAR: Estimated number of people which is Union : %d' % union_count_linear

#logit
y_hat_logit = results_logit.predict(X_pred)
union_count_logit = 0
for people in y_hat_logit:
  if float(people) > 0.25: union_count_logit += 1
print 'LOGIT : Estimated number of people which is Union : %d\n\n' % union_count_logit

