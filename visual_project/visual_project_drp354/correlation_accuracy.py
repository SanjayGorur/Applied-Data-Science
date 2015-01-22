##############################################
##############################################
#      Applied Data Science/ fall 2014       # 
#      Video Project (Final)                 #
#      Dimas Rinarso Putro | drp354@nyu.edu  #
#      correlation_accuracy.py               #
##############################################

import os
import time
import sys
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as nd
from scipy.ndimage.filters import median_filter as mf


img = nd.imread('images/digits.png')
nrow, ncol = img.shape[0:2]
xs = 10.
ys = xs*float(nrow)/float(ncol)

nums = img.reshape(50,20,100,20).transpose(0,2,1,3).reshape(5000,20,20)
nums_avg0 = np.array([nums[i*500:(i+1)*500].mean(0) for i in range(10)])
nums_avg = nums_avg0
c = 0
for x in nums_avg:
	mean = x.reshape(-1).mean()
	std = x.reshape(-1).std()
	x = (x - mean)/std
	x.reshape(20,20)
	nums_avg[c] = x
	c += 1

rslt = [[] for i in range(10)]
acr = []
error = []
PT = nums_avg.reshape(10,400)
P  = PT.transpose()
PTPinv = np.linalg.inv(np.dot(PT,P))

for i in range(5000):
	n = i/500
	samp = nums[i]
	PTyy = np.dot(PT,samp.flatten())
	avec = np.dot(PTPinv,PTyy)
	rslt[n].append(list(avec))
	error.append(avec.argmax())
error = np.array(error).reshape(10,500)

for i in range(10):
    fig = plt.figure()
    m = np.array(rslt[i])
    for j in range(10):
        r = m[:,j]
        ax = fig.add_subplot(5,2,j+1)
        ax.set_title('distribution of the number {0}'.format(j))
        ax.hist(r,bins=100,alpha = 0.7)
plt.tight_layout()
plt.show()

# problem2
for i in range(10):
	n = len(error[i,:][error[i,:]!=i])
	errdct = dict((x,list(error[i,:]).count(x)) for x in set(list(error[i,:])))
	del errdct[i]
	mx =max(errdct,key=errdct.get)
	print "%s"%(n/5,)+'%'+"of %s's were incorrectly identified, the most common guess for those failures was %s"%(i, mx)
