#################################################
# Kania Azrina | N13602569 | ka1531@nyu.edu		
# Yixue Wang | N12334680 | yw1918@nyu.edu   
# CUSP GX 5004 Applied Data Science	  
# Image Processing Final Project						
# image_exploration_bonus.py								
#################################################

import os
import sys
import time
import pylab
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as nd
from scipy.ndimage.filters import median_filter as mf

def tellme(s,fig):
    print(s)
    fig.suptitle(s,fontsize=10)
    plt.draw()

def explore(folder,filename):
	#Task 1
	#display the image in a figure (again, taking up the full window 
	#frame and setting the title of the window to be the filename)
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

	#Task 2
	#in a separate window display three panels, in the first panel 
	#plot the histogram of the red channel using red bars with range 
	#[0,255] and 256 bins, in the second panel, plot the histogram of 
	#the green channel using green bars range [0,255] and 256 bins, and 
	#in the third panel plot the histogram of the blue channel using blue 
	#bars with range [0,255] and 256 bins.
	labels = ['Red Channel', 'Green Channel','Blue Channel']
	colors = ['Red', 'Green','Blue']
	fig0, ax0 = plt.subplots(3,1,num=0,figsize=[8,8])
	fig0.canvas.set_window_title('Image Exploration Widget')
	
	for i in range(3):
	    ax0[i].hist((np.array(img_ml[:,:,i]).reshape(-1,).tolist()), bins=256, histtype='bar', color= colors[i],alpha = 0.8, label=labels[i],linewidth=0)
	    ax0[i].legend()
	    ax0[i].set_xlim(0,255)

	#tellme("Click three values from each channel",fig0)

	plt.show()	

	mode = ["range","darken"]
	button_pressed = False
	cur_mod = 1 #set default mode

	#3. in an infitinte loop, use the ginput() function to select three 
	#values from the histogram panels (one from each histogram)
	while True:
		string = "Current mode : "+mode[cur_mod]+", press button key to change mode. Click in widget to continue."
		tellme(string,fig0)
		button_pressed = fig0.waitforbuttonpress()
		print button_pressed

		if button_pressed :
			if cur_mod ==1 :
				button_pressed = False
				print "nyaw"
				cur_mod =0
				string = "Mode changed, current mode : range. Select two points in the image."
			elif cur_mod==0:
				button_pressed = False
				cur_mod=1
				string = "Mode changed, current mode : darken. Select three values from each channel."
			
			tellme(string,fig0)

		if (cur_mod == 0):
			#tellme("Select two points in the image.",fig0)
			temp = fig1.ginput(2)
			tellme("Please Wait....",fig0)
		   	#Task 4
			#update the histograms for each color channel to only display the 
			#values within the region selected in 3
			
			#Task 5
			#double clicking (i.e., clicking the same pixel twice) should reset 
			#the histograms to be for those of the full image
			if int(temp[0][0])==int(temp[1][0]) and int(temp[0][1])==int(temp[1][1]):
				fig0.clear()
				fig0, ax0 = plt.subplots(3,1,num=0,figsize=[8,8])
				for i in range(3):
					ax0[i].hist((np.array(img_ml[:,:,i]).reshape(-1,).tolist()), bins=256, histtype='bar', color= colors[i],alpha = 0.8, label=labels[i],linewidth=0)
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
					ax0[i].hist(hist_new[i],bins=256,color = colors[i],alpha = 0.8, label=labels[i],linewidth=0)
					ax0[i].set_xlim(0,255)
					ax0[i].legend()

	
		if (cur_mod == 1):
		    #tellme("Select three values from each channel.",fig0)
		    img_ml = nd.imread(imagefile)
		    temp = fig0.ginput(3)
		    tellme("Please Wait....",fig0)
		    
		    #4. draw highlighted regions around the selected values (see the 
		    #"Filtering re-explained" in the ipython notebook dobler_112414_part1.ipynb 
		    #for drawing semi-transparent rectangles which span the full y-axis) in each histogram. 
		    #The highlighting should be centered on the selected value and have a width of 10
		    source = []	    	    
		    source = img_ml	    
		    fig0.clear()
		    fig0, ax0 = plt.subplots(3,1,num=0,figsize=[8,8])
		    
		    for i in range(3):
		        hist_range = []
		        hist_range = (np.array(source[:,:,i]).reshape(-1,).tolist())
		        ax0[i].hist(hist_range, 256, histtype='bar', color= colors[i],alpha = 0.8,label=labels[i],linewidth=0)
		        ax0[i].legend()
		        ax0[i].set_xlim(0,255)
		        ax0[i].axvspan((temp[i][0]-5),(temp[i][0]+5),facecolor='yellow',alpha=0.25,linewidth=0)
		

			#5. darken (by 75%) all pixels in the image which fall outside of 
			#+/- 5 from the selected values in 3.

			#6. the user should be able to repeat step 3 (which triggers 4 and 5) 
			#as many times as s/he wishes

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
    explore(folder,filename)