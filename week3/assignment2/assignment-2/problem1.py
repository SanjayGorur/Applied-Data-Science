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

###No.1a###
###########################################
#variable initialization
mu, sigma = 0, 1
num_samples = 10 #change this value for number 1a-1c

#generate random numbers
nor = np.random.normal(mu, sigma, num_samples)
#calculate mean
print 'Mean = ',str(np.mean(nor))
#verify the standard deviation
print 'Variance = ',str(np.var(nor, ddof=1))
#verify the standard deviation
print 'Standard Deviation = ',str(np.std(nor, ddof=1))

#plot histogram
count, bins, ignored = plt.hist(nor, 30, normed=True)
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
               np.exp( - (bins - mu)**2 / (2 * sigma**2) ),
         linewidth=2, color='r')
plt.show()