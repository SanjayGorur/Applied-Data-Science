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

###No.5###
###########################################
#variable initialization
mu, sigma = 0, 1
num_samples = 1000

#generate random numbers
x = np.random.normal(mu, sigma, num_samples)
e = np.random.normal(mu, sigma, num_samples)
y = 1+2*x+e

#regression
x = sm.add_constant(x)
model = sm.OLS(y, x)
results = model.fit()
print(results.summary())

###########################################
###########NOW WITH MONTE CARLO############
#---------5 iterations
m = []
for i in xrange (0,4):
  #generate random numbers
  x = np.random.normal(mu, sigma, num_samples)
  e = np.random.normal(mu, sigma, num_samples)
  y = 1+2*x+e

  #regression
  regression = np.polyfit(x, y, 1)
  m.append(regression[0]) #adding beta into list

print 'Beta value for 5 iterations: '+str(m)

###########################################
###########NOW WITH MONTE CARLO############
#---------1000 iterations
m_1000 = []
for i in xrange (0,999):
  #generate random numbers
  x = np.random.normal(mu, sigma, num_samples)
  e = np.random.normal(mu, sigma, num_samples)
  y = 1+2*x+e

  #regression
  regression = np.polyfit(x, y, 1)
  m_1000.append(regression[0]) #adding beta into list

#plot histogram
acount, bins, ignored = plt.hist(m_1000, 100, normed=True)
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
               np.exp( - (bins - mu)**2 / (2 * sigma**2) ),
         linewidth=2, color='r')
plt.show()

###########################################
###########NOW WITH MONTE CARLO############
#---------1000 iterations on exp(Beta)
m_1000 = []
for i in xrange (0,999):
  #generate random numbers
  x = np.random.normal(mu, sigma, num_samples)
  e = np.random.normal(mu, sigma, num_samples)
  y = 1+2*x+e

  #regression
  regression = np.polyfit(x, y, 1)
  m_1000.append(np.exp(regression[0])) #adding beta into list

#plot histogram
acount, bins, ignored = plt.hist(m_1000, 100, normed=True)
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
               np.exp( - (bins - mu)**2 / (2 * sigma**2) ),
         linewidth=2, color='r')
plt.show()
