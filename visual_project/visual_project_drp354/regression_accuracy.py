##############################################
##############################################
#      Applied Data Science/ fall 2014       # 
#      Video Project (Final)                 #
#      Dimas Rinarso Putro | drp354@nyu.edu  #
#      regression_accuracy.py                #
##############################################

import os
import time
import sys
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as nd
from scipy.ndimage.filters import median_filter as mf
from random import randrange
import operator
import random

img = nd.imread('images/digits.png')
nrow, ncol = img.shape[0:2]
xs = 10.
ys = xs*float(nrow)/float(ncol)
nums = img.reshape(50,20,100,20).transpose(0,2,1,3).reshape(5000,20,20)
nums_avg = np.array([nums[i*500:(i+1)*500].mean(0) for i in range(10)])

#### problem1
rslt = [[] for i in range(10)]
acr = []
error = []
PT = nums_avg.reshape(10,400)
P  = PT.transpose()
PTPinv = np.linalg.inv(np.dot(PT,P))
	
for i in range(len(nums)):
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
	print "%s of %s's were incorrectly identified, the most common guess for those failures was %s"%(n/500., i, mx)

# problem3 
plt.ion()
n = [[],[]]
for i in range(10):
	c = 0
 	for j in random.sample(xrange(500),500):
 		if c < 4 and error[i][j] != i: 
 			dsp = error[i][j]
 			c += 1
 			n[0].append(i*500 + j)
 			n[1].append(dsp)

fig1, ax1 = plt.subplots(2,1)
ax1[1].axis('off')
ax1[0].axis('off')
ax1[0].set_title('failures')
ax1[1].set_title('guess')
im1 = ax1[0].imshow(nums[0])
im2 = ax1[1].imshow(nums[0])

t0 = time.time()
dt = 0.0
while dt<30.:
	for i in range(len(n[1])):
		im1.set_data(nums[n[0][i]])
 		im2.set_data(nums_avg[n[1][i]])
 		fig1.canvas.draw()
 		time.sleep(1)
 		dt = time.time()-t0
 		plt.show()

#problem4
plt.ioff()
rslt = [[] for i in range(10)]
acr = []
error = []
PT = nums_avg.reshape(10,400)
PT = np.vstack((PT,np.ones(400))) 
P  = PT.transpose()
PTPinv = np.linalg.inv(np.dot(PT,P))
	
for i in range(5000):
	n = i/500
	samp = nums[i]
	PTyy = np.dot(PT,samp.flatten())
	avec = np.dot(PTPinv,PTyy)[:10]
	rslt[n].append(list(avec))
	error.append(avec.argmax())
error = np.array(error).reshape(10,500)

for i in range(10):
	n = len(error[i,:][error[i,:]!=i])
	errdct = dict((x,list(error[i,:]).count(x)) for x in set(list(error[i,:])))
	del errdct[i]
	mx =max(errdct,key=errdct.get)
	print "%s of %s's were incorrectly identified, the most common guess for those failures was %s"%(n/500., i, mx)