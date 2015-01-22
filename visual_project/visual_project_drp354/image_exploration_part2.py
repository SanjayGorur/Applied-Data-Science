##############################################
##############################################
#      Applied Data Science/ fall 2014       # 
#      Video Project (Final)                 #
#      Dimas Rinarso Putro | drp354@nyu.edu  #
#      image_exploration_part2.py            #
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
	    histX = (np.array(img_ml[:,:,i]).reshape(-1,).tolist())
	    ax0[i].hist(histX, nbin, histtype='bar', color= colors[i],alpha = 0.8, label=colors[i],edgecolor=colors[i])
	    ax0[i].legend(prop={'size': 10})
	    ax0[i].set_xlim(0,255)
	fig0.canvas.draw()
	        
	fig5, ax5 = plt.subplots(num=5,figsize=[xsize,ysize])
	fig5.subplots_adjust(0,0,1,1)
	ax5.axis('off')
	im5 = ax5.imshow(img_ml)
	fig5.canvas.draw()

	plt.show()

	
	while True:
	    img_ml = nd.imread(infile)
	    temp = fig0.ginput(3)

	    img_ml_source = []	    	    
	    img_ml_source = img_ml	    
	    fig0.clear()
	    fig0, ax0 = plt.subplots(num,1,num=0,figsize=[8,8])
	    for i in range(num):
	        histX = []
	        histX = (np.array(img_ml_source[:,:,i]).reshape(-1,).tolist())
	        ax0[i].hist(histX, nbin, histtype='bar', color= colors[i],alpha = 0.8,label=colors[i],edgecolor=colors[i])
	        ax0[i].legend(prop={'size': 10})
	        ax0[i].set_xlim(0,255)
	        ax0[i].axvspan((temp[i][0]-5),(temp[i][0]+5),facecolor='lime',alpha=0.25)

	            
	    x = []
	    y = []
	    img_ml_darken = []
	    img_ml_darken = img_ml
	    for i in range(len(temp)):
	        x.append(int(temp[i][0]))
	        y.append(int(temp[i][1]))
	        for i in range(img_ml.shape[0]):
	            for j in range(img_ml.shape[1]):
	                r,g,b = img_ml[i][j]
	                if (r<(temp[0][0]-5) or r>(temp[0][0]+5))\
	                and (g<(temp[1][0]-5) or g>(temp[1][0]+5))\
	                and (b<(temp[2][0]-5) or b>(temp[2][0]+5)):
	                    img_ml_darken[i][j]=(.25*r,.25*g,.25*b)
	    fig5.clear() 
	    fig5, ax5 = plt.subplots(num=5,figsize=[xsize,ysize])
	    fig5.subplots_adjust(0,0,1,1)
	    ax5.axis('off')
	    im5 = ax5.imshow(img_ml_darken)
	    plt.show()    

if __name__ == '__main__':
    foldername = sys.argv[1]
    filename   = sys.argv[2]
    main(foldername,filename)
