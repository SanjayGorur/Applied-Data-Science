##############################################
##############################################
#      Applied Data Science GX5004           # 
#      Assignment 3                          #
#      Dimas Rinarso Putro | drp354@nyu.edu  #
#      No.1b,c,d,e                           #
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
plt.xlabel('rns')
plt.ylabel('Log Wage')
plt.title('ls VS rns');
plt.savefig('1-lw-VS-rns.png')
#plt.show()

#=====================
#lw VS mrt 
#=====================
#plot the linear regression
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
plt.xlabel('mrt')
plt.ylabel('Log Wage')
plt.title('ls VS mrt');
plt.savefig('1-lw-VS-mrt.png')
#plt.show()


#=====================
#lw VS smsa 
#=====================
#plot the linear regression
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
plt.xlabel('smsa')
plt.ylabel('Log Wage')
plt.title('ls VS smsa');
plt.savefig('1-lw-VS-smsa.png')
#plt.show()


#=====================
#lw VS kww 
#=====================
#plot the linear regression
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
plt.xlabel('kww')
plt.ylabel('Log Wage')
plt.title('ls VS kww');
plt.savefig('1-lw-VS-kww.png')
#plt.show()

#=====================
#lw VS expr 
#=====================
#plot the linear regression
x = df.expr
y = df.lw
X = sm.add_constant(x)
model = sm.OLS(y, X)
results = model.fit()
print(results.summary())
plt.figure();
plt.plot(x, y, 'o');
prstd, iv_l, iv_u = wls_prediction_std(results)
plt.plot(x, results.fittedvalues, 'b--.')
plt.xlabel('expr')
plt.ylabel('Log Wage')
plt.title('ls VS expr');
plt.savefig('1-lw-VS-expr.png')
#plt.show()

#=====================
#lw VS s 
#=====================
#plot the linear regression
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
