##############################################
##############################################
#      Applied Data Science/ fall 2014       # 
#      Video Project (Final)                 #
#      Dimas Rinarso Putro | drp354@nyu.edu  #
#      image_exploration_part1.py            #
##############################################

import os
import sys
import time
import pylab
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as nd
from scipy.ndimage.filters import median_filter as mf


def main(foldername,filename):

	infile = os.path.join(foldername,filename)
	plt.ion()
	img_ml = nd.imread(infile)

	num = 3
	nbin = 256
	colors = ['red', 'green','blue']
	fig0, ax0 = plt.subplots(num,1,num=0,figsize=[8,8])
	ysize = 10.
	xsize = ysize*float(img_ml.shape[1])/float(img_ml.shape[0])

	for i in range(num):
	    ax0[i].hist((np.array(img_ml[:,:,i]).reshape(-1,).tolist()), nbin, histtype='bar', color= colors[i],alpha = 0.8, label=colors[i],edgecolor=colors[i])
	    ax0[i].legend(prop={'size': 10})
	    ax0[i].set_xlim(0,255)

	fig5, ax5 = plt.subplots(num=5,figsize=[xsize,ysize])
	fig5.subplots_adjust(0,0,1,1)
	ax5.axis('off')
	im5 = ax5.imshow(img_ml)

	plt.show()	
	
	while True:
	    print 'entering'
	    temp = fig5.ginput(2)
	    print temp

	    if int(temp[0][0])==int(temp[1][0]) and int(temp[0][1])==int(temp[1][1]):
	        fig0.clear()
	        fig0, ax0 = plt.subplots(num,1,num=0,figsize=[8,8])
	        for i in range(num):
	            ax0[i].hist((np.array(img_ml[:,:,i]).reshape(-1,).tolist()), nbin, histtype='bar', color= colors[i],alpha = 0.8, label=colors[i],edgecolor=colors[i])
	            ax0[i].legend(prop={'size': 10})
	            ax0[i].set_xlim(0,255)

	    else:
	        x = []
	        y = []
	        for i in range(len(temp)):
	            x.append(int(temp[i][0]))
	            y.append(int(temp[i][1]))
	        img_ml_crop = img_ml[np.min(y):np.max(y),np.min(x):np.max(x)]
	        histogram_crop = [],[],[]
	        for i in range(img_ml_crop.shape[0]):
	            for j in range(img_ml_crop.shape[1]):
	                histogram_crop[0].append(img_ml_crop[i,j][0])
	                histogram_crop[1].append(img_ml_crop[i,j][1])
	                histogram_crop[2].append(img_ml_crop[i,j][2])
	        fig0.clear()
	        fig0, ax0 = plt.subplots(num,1,num=0,figsize=[8,8])
	        for i in range(num):
	            ax0[i].hist(histogram_crop[i],bins=256,color = colors[i],alpha = 0.8, label=colors[i],edgecolor=colors[i])
	            ax0[i].legend(prop={'size': 10})
	            ax0[i].set_xlim(0,255)
    

if __name__ == '__main__':
    foldername = sys.argv[1]
    filename   = sys.argv[2]
    main(foldername,filename)
