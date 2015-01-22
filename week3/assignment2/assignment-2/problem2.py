##############################################
##############################################
#      Applied Data Science GX5004           # 
#      Assignment 2                          #
#      Dimas Rinarso Putro | drp354@nyu.edu  #
##############################################

import argparse,csv, sys, os
import numpy as np
from matplotlib import pyplot as plt
import pylab
import statsmodels.api as sm

###No.2###
###########################################
#variable initialization
mu, sigma = 0, 1
num_samples = 1000000
filename='no-2.csv'
x = []
y = []

with open(filename, 'rb') as f:
   csvReader = csv.reader(f)
   headers = next(csvReader)
   for row in csvReader:
       x.append(int(row[0]))
       y.append(int(row[1]))

print x
print y

##t-statistic
# Fit regression model
x = sm.add_constant(x)
results = sm.OLS(y, x).fit()
# Inspect the results
print results.summary()

"""
##plotting the files
regression = np.polyfit(x, y, 1)
reg = np.poly1d(regression)
plt.plot(x, y, '.', x, reg(x), '--')
plt.xlabel('x')
plt.ylabel('y')
plt.xlim(0, 10)
plt.ylim(0, 10)
plt.show()
"""


