##############################################
##############################################
#      Applied Data Science GX5004           # 
#      Assignment 2                          #
#      Dimas Rinarso Putro | drp354@nyu.edu  #
#      No.1                                  #
##############################################

import argparse,csv,sys,os
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
from pandas.tools.plotting import scatter_matrix as scatter
from pandas.io.stata import read_stata as rd_stata
import statsmodels.api as sm
from statsmodels.sandbox.regression.predstd import wls_prediction_std

###No.4###
##############################################

#Read data
filename = 'griliches.dta'
df = rd_stata(filename)

#============print the summary for each column
print 'rns ='
print df['rns'].describe()
print 'mrt ='
print df['mrt'].describe()
print 'smsa ='
print df['smsa'].describe()
print 'med ='
print df['med'].describe()
print 'iq ='
print df['iq'].describe()
print 'kww ='
print df['kww'].describe()
print 'age ='
print df['age'].describe()
print 's ='
print df['s'].describe()
print 'expr ='
print df['expr'].describe()
print 'lw ='
print df['lw'].describe()


#===========Least square regression
#=====================
#lw VS rns 
#=====================
#plot the linear regression
#and also the confidence level
x = df.rns
y = df.lw
X = sm.add_constant(x)
model = sm.OLS(y, X)
results = model.fit()
print(results.summary())
plt.figure();
plt.plot(x, y, 'o');
prstd, iv_l, iv_u = wls_prediction_std(results)
plt.plot(x, results.fittedvalues, 'b--.')
#plt.plot(x, iv_u, 'r--')
#plt.plot(x, iv_l, 'r--')
plt.xlabel('rns')
plt.ylabel('Log Wage')
plt.title('ls VS rns');
plt.savefig('1-lw-VS-rns.png')
#plt.show()

#=====================
#lw VS mrt 
#=====================
#plot the linear regression
#and also the confidence level
x = df.mrt
y = df.lw
X = sm.add_constant(x)
model = sm.OLS(y, X)
results = model.fit()
print(results.summary())
plt.figure();
plt.plot(x, y, 'o');
prstd, iv_l, iv_u = wls_prediction_std(results)
plt.plot(x, results.fittedvalues, 'b--.')
#plt.plot(x, iv_u, 'r--')
#plt.plot(x, iv_l, 'r--')
plt.xlabel('mrt')
plt.ylabel('Log Wage')
plt.title('ls VS mrt');
plt.savefig('1-lw-VS-mrt.png')
#plt.show()


#=====================
#lw VS smsa 
#=====================
#plot the linear regression
#and also the confidence level
x = df.smsa
y = df.lw
X = sm.add_constant(x)
model = sm.OLS(y, X)
results = model.fit()
print(results.summary())
plt.figure();
plt.plot(x, y, 'o');
prstd, iv_l, iv_u = wls_prediction_std(results)
plt.plot(x, results.fittedvalues, 'b--.')
#plt.plot(x, iv_u, 'r--')
#plt.plot(x, iv_l, 'r--')
plt.xlabel('smsa')
plt.ylabel('Log Wage')
plt.title('ls VS smsa');
plt.savefig('1-lw-VS-smsa.png')
#plt.show()


#lw VS kww 
#=====================
#lw VS kww 
#=====================
#plot the linear regression
#and also the confidence level
x = df.kww
y = df.lw
X = sm.add_constant(x)
model = sm.OLS(y, X)
results = model.fit()
print(results.summary())
plt.figure();
plt.plot(x, y, 'o');
prstd, iv_l, iv_u = wls_prediction_std(results)
plt.plot(x, results.fittedvalues, 'b--.')
#plt.plot(x, iv_u, 'r--')
#plt.plot(x, iv_l, 'r--')
plt.xlabel('kww')
plt.ylabel('Log Wage')
plt.title('ls VS kww');
plt.savefig('1-lw-VS-kww.png')
#plt.show()


#=====================
#lw VS s 
#=====================
#plot the linear regression
#and also the confidence level
x = df.s
y = df.lw
X = sm.add_constant(x)
model = sm.OLS(y, X)
results = model.fit()
print(results.summary())
plt.figure();
plt.plot(x, y, 'o');
prstd, iv_l, iv_u = wls_prediction_std(results)
plt.plot(x, results.fittedvalues, 'g--.')
plt.plot(x, iv_u, 'r--')
plt.plot(x, iv_l, 'r--')
plt.xlabel('s')
plt.ylabel('Log Wage')
plt.title('ls VS s');
plt.savefig('1-lw-VS-s.png')
#plt.show()


