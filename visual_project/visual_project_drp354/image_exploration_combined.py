##############################################
##############################################
#      Applied Data Science/ fall 2014       # 
#      Video Project (Final)                 #
#      Dimas Rinarso Putro | drp354@nyu.edu  #
#      image_exploration_combined.py         #
##############################################

import os
import sys
import time
import pylab
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as nd
from scipy.ndimage.filters import median_filter as mf

def displayTitle(s,fig):
    print(s)
    fig.suptitle(s,fontsize=10)
    plt.draw()

def main(folder,filename):
	plt.ion()
	imagefile = os.path.join(folder,filename)
	img_ml = nd.imread(imagefile)
	ysize = 10.
	xsize = ysize*float(img_ml.shape[1])/float(img_ml.shape[0])
	fig1, ax1 = plt.subplots(num=5,figsize=[xsize,ysize])
	fig1.subplots_adjust(0,0,1,1)
	ax1.axis('off')
	im1 = ax1.imshow(img_ml)
	fig1.canvas.set_window_title(filename)

	colors = ['Red','Green','Blue']
	fig0, ax0 = plt.subplots(3,1,num=0,figsize=[8,8])
	fig0.canvas.set_window_title('Image Exploration Widget')
	
	for i in range(3):
	    ax0[i].hist((np.array(img_ml[:,:,i]).reshape(-1,).tolist()), bins=256, histtype='bar', color= colors[i],alpha = 0.8, label=colors[i],edgecolor=colors[i])
	    ax0[i].legend()
	    ax0[i].set_xlim(0,255)

	plt.show()	

	mode = ["range","darken"]
	button_pressed = False
	cur_mod = 0 

	while True:
		string = "MODE : "+mode[cur_mod]+", press any button in this window to shift mode."
		displayTitle(string,fig0)
		button_pressed = fig0.waitforbuttonpress()
		print button_pressed

		if button_pressed :
			if cur_mod ==1 :
				cur_mod =0
				button_pressed = False
			elif cur_mod == 0:
				cur_mod=1
				button_pressed = False
			string = "[Mode Changed] MODE : "+mode[cur_mod]+", press any button in this window to shift mode."
			displayTitle(string,fig0)

		if (cur_mod == 0):
			temp = fig1.ginput(2)

			if int(temp[0][0])==int(temp[1][0]) and int(temp[0][1])==int(temp[1][1]):
				fig0.clear()
				fig0, ax0 = plt.subplots(3,1,num=0,figsize=[8,8])
				for i in range(3):
					ax0[i].hist((np.array(img_ml[:,:,i]).reshape(-1,).tolist()), bins=256, histtype='bar', color= colors[i],alpha = 0.8, label=colors[i],edgecolor=colors[i])
					ax0[i].legend()
					ax0[i].set_xlim(0,255)
			else:
				x = []
				y = []
				for i in range(len(temp)):
					x.append(int(temp[i][0]))
					y.append(int(temp[i][1]))
				img_ml_new = img_ml[np.min(y):np.max(y),np.min(x):np.max(x)]
				hist_new = [],[],[]
				for i in range(img_ml_new.shape[0]):
					for j in range(img_ml_new.shape[1]):
						hist_new[0].append(img_ml_new[i,j][0])
						hist_new[1].append(img_ml_new[i,j][1])
						hist_new[2].append(img_ml_new[i,j][2])
				fig0.clear()
				fig0, ax0 = plt.subplots(3,1,num=0,figsize=[8,8])
				for i in range(3):
					ax0[i].hist(hist_new[i],bins=256,color = colors[i],alpha = 0.8, label=colors[i],edgecolor=colors[i])
					ax0[i].set_xlim(0,255)
					ax0[i].legend()

	
		if (cur_mod == 1):
		    img_ml = nd.imread(imagefile)
		    temp = fig0.ginput(3)
		    
		    source = []	    	    
		    source = img_ml	    
		    fig0.clear()
		    fig0, ax0 = plt.subplots(3,1,num=0,figsize=[8,8])
		    
		    for i in range(3):
		        hist_range = []
		        hist_range = (np.array(source[:,:,i]).reshape(-1,).tolist())
		        ax0[i].hist(hist_range, 256, histtype='bar', color= colors[i],alpha = 0.8,label=colors[i],edgecolor=colors[i])
		        ax0[i].legend()
		        ax0[i].set_xlim(0,255)
		    	ax0[i].axvspan((temp[i][0]-5),(temp[i][0]+5),facecolor='lime',alpha=0.25)

			x = []
		    y = []
		    darken = []
		    darken = img_ml
		    for i in range(len(temp)):
		        x.append(int(temp[i][0]))
		        y.append(int(temp[i][1]))
		        for i in range(img_ml.shape[0]):
		            for j in range(img_ml.shape[1]):
		                r,g,b = img_ml[i][j]
		                if (r<(temp[0][0]-5) or r>(temp[0][0]+5)) and (g<(temp[1][0]-5) or g>(temp[1][0]+5)) and (b<(temp[2][0]-5) or b>(temp[2][0]+5)):
		                    darken[i][j]=(.25*r,.25*g,.25*b)
		    fig1.clear() 
		    fig1, ax1 = plt.subplots(num=5,figsize=[xsize,ysize])
		    fig1.subplots_adjust(0,0,1,1)
		    ax1.axis('off')
		    im1 = ax1.imshow(darken)
		    plt.show() 

if __name__ == '__main__':
    folder = sys.argv[1]
    filename   = sys.argv[2]
    main(folder,filename)
