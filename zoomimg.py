import cv2
import numpy as np
import sys

#from math import *

def zoom(imgpath,x_coord,y_coord,scale):

	#x_coord = 1024
	#y_coord = 640
	#scale=1

	img=cv2.imread(imgpath)

	tl_x = int(x_coord - (float(1)/float(scale) * float(1)/float(2) * img.shape[1]))
	tl_y = int(y_coord - (float(1)/float(scale) * float(1)/float(2) * img.shape[0]))

	#br_x = int(x_coord + (float(1)/float(scale) * float(1)/float(2) * img.shape[1]))
	#br_y = int(x_coord + (float(1)/float(scale) * float(1)/float(2) * img.shape[0]))

	br_x = int(tl_x + (float(1)/float(scale) * img.shape[1]))
	br_y = int(tl_y + (float(1)/float(scale) * img.shape[0]))

	#print tl_x
	#print tl_y

	#print br_x
	#print br_y

	if (tl_x < 0):
		br_x = br_x - tl_x
		tl_x = 0
	if (tl_y < 0):
		br_y = br_y - tl_y
		tl_y = 0

	if (br_x > img.shape[1]):
		tl_x = tl_x - (br_x - img.shape[1])
		br_x = img.shape[1]
	if (br_y > img.shape[0]):
		tl_y = tl_y - (br_y - img.shape[0])
		br_y = img.shape[0]

	'''
	if(tl_x < 0):
		if(tl_y < 0):
			br_x -= tl_x
			br_y -= tl_y
			tl_x=0
			tl_y=0
		else:
			if(br_y <= img.shape[1]):
				br_x -= tl_x
				tl_x = 0
			else:
				br_x -= tl_x
				tl_x = 0
				tl_y -= (br_y - img.shape[1])
				br_y = img.shape[1]
	else:
	'''
	'''
	if((tl_x < 0) && (tl_y < 0)):
		br_x -= tl_x
		br_y -= tl_y
		tl_x=0
		tl_y=0
	elif ((tl_x >= 0) && (tl_x <= img.shape[0]) && (tl_y < 0) && (br_x > img.shape[0])):
		tl_x -= (br_x-img.shape[0])
		br_x = img.shape[0]
		br_y -= tl_y
		tl_y = 0
	elif ((tl_x >= 0) && (tl_x <= img.shape[0]) && (tl_y < 0)):
		br_y -= tl_y
		tl_y = 0
	elif 

	if (tl_x <  0):
		#br_x -= tl_x
		tl_x=0
		br_x = int((float(1)/float(scale)) * img.shape[0])
	
	if (tl_y < 0):
		#br_y -= tl_y
		tl_y=0
		br_y = int((float(1)/float(scale)) * img.shape[1])

	if (br_x > img.shape[0]):
		#extra_x = br_x-img.shape[0]
		#tl_x -= extra_x
		br_x = img.shape[0]
		tl_x -= int((float(1)/float(scale)) * img.shape[0])

	if (br_y > img.shape[1]):
		#extra_y = br_y-img.shape[1]
		#tl_y -= extra_y
		br_y = img.shape[1]
		tl_y -= int((float(1)/float(scale)) * img.shape[1])
	'''
	#print tl_x
	#print tl_y

	#print br_x
	#print br_y

	roi=img[tl_y:br_y, tl_x:br_x,:]
	#roi = img[50:52,50:52]
	#print roi.shape
	#newimg=copy.deepcopy(roi)
	#print newimg.shape

	#newimg_shape=newimg.shape
	width1=(roi.shape[1])-1
	height1=(roi.shape[0])-1

	#width2 = newimg.shape[0] + 400
	#height2 = newimg.shape[1] + 400

	width2 = img.shape[1]
	height2 = img.shape[0]

	#width2 = 5
	#height2 = 5

	width_ratio=float(width1)/float(width2)
	height_ratio=float(height1)/float(height2)

	count=0
	new=[]
	#new.append([])
	#temp_height2=height2+179
	#temp_width2=width2+179

	for i in range((height2)):
		for j in range((width2)):
			x = int(width_ratio*j)
			y = int(height_ratio*i)
			x_diff = (width_ratio*j) - x
			y_diff = (height_ratio*i) - y
			#print "x: "+str(x)
			#print "j: "+str(j)
			#print "y: "+str(y)
			#print "i: "+str(i)
			#print "Width: "+str(width2)
			#print "Height: "+str(height2)
			#print "IMG shape: "+str(img.shape)
			#print "ROI shape: "+str(roi.shape)
			#[x][y]

			if (x>=(width1-1) or y>=(height1-1)):
				#print "A in"
				A_blue = roi[y][x][0]
				A_red = roi[y][x][1]
				A_green = roi[y][x][2]
			else:
				#print "A out"
				A_blue = roi[y][x][0]
				A_red = roi[y][x][1]
				A_green = roi[y][x][2]
				#A = roi[y][x][:] & 0xff

			if ((x+1)>=(width1-1) or (y>=(height1-1))):
				#print "B in"
				B_blue = roi[y][x][0]
				B_red = roi[y][x][1]
				B_blue = roi[y][x][2]
			else:
				#print "B out"
				B_blue = roi[y+1][x][0] & 0xff
				B_red = roi[y+1][x][1]
				B_green = roi[y+1][x][2]
			if (x>=(width1-1) or ((y+1)>=(height1-1))):
				#print "C in"
				C_blue = roi[y][x][0]
				C_red = roi[y][x][1]
				C_green = roi[y][x][2]
			else:
				#print "C  out"
				#print roi.shape
				C_blue = roi[y][x+1][0] & 0xff
				C_red = roi[y][x+1][1]
				C_green = roi[y][x+1][2]
			if ((x+1)>=(width1-1) or (y+1)>=(height1-1)):
				#print "D in"
				D_blue = roi[y][x][0] & 0xff
				D_red = roi[y][x][1]
				D_green = roi[y][x][2]
			else:
				#print "D out"
				D_blue = roi[y+1][x+1][0] & 0xff
				D_red = roi[y+1][x+1][1]
				D_green = roi[y+1][x+1][2]
			#print A
			#print B
			#print "D in"
			#print C
			#print D
			#print "D out"

			gray_blue = (int) ( (A_blue * (1 - x_diff) * (1 - y_diff)) + (B_blue * (x_diff) * (1 - y_diff)) + (C_blue * (y_diff)*(1 - x_diff)) + (D_blue * (x_diff*y_diff)))
			gray_red = (int) ( (A_red * (1 - x_diff) * (1 - y_diff)) + (B_red * (x_diff) * (1 - y_diff)) + (C_red * (y_diff)*(1 - x_diff)) + (D_red * (x_diff*y_diff)))
			gray_green = (int) ( (A_green * (1 - x_diff) * (1 - y_diff)) + (B_green * (x_diff) * (1 - y_diff)) + (C_green * (y_diff)*(1 - x_diff)) + (D_green * (x_diff*y_diff)))				

			#print "Gray\n"
			#print gray

			newrow=count/(width2)
			newcol=count%(width2)
	#		print "\nNewrow: "+str(newrow)
	#		print "\nNewcol: "+str(newcol)
	#		print img.shape
	#		print count
	#		print height2
	#		print width2
			finalgray = [gray_blue,gray_red,gray_green]
			if(newcol == 0):
				new.append([])
			new[newrow].append(finalgray)
			#rew[newrow][newcol]=gray
			count+=1

	#print new
	#print roi
	final_img=np.uint8(new)
	#print final_img
	#print img.shape
	#print final_img.shape
	return final_img

if __name__=="__main__":
	path = sys.argv[1]
	img=cv2.imread(path)

	x_coord = int(sys.argv[2])
	y_coord = int(sys.argv[3])
	scale = int(sys.argv[4])

	final_img=zoom(path,x_coord,y_coord,scale)
	cv2.imshow('Original',img)
	cv2.imshow('Final',final_img)
	#newfinal=cv2.cvtColor(final_img,cv2.COLOR_GRAY2BGR)
	#cv2.imshow('NEW',newfinal)
	cv2.waitKey(0)
	cv2.destroyAllWindows()