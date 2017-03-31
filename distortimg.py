import cv2
import numpy as np
import sys

# Function to distort a given image, to the given co-ordinates
# imgpath - path of given image
# x1_coord, y1_coord ... x4_coorf, y4_coord, are the given co-ordinated to which the given image is to be distorted to
def distortimg(imgpath,x1_coord,y1_coord,x2_coord,y2_coord,x3_coord,y3_coord,x4_coord,y4_coord):

	img=cv2.imread(imgpath)

	shape = img.shape

	# Existing end co-ordinates of the given image
	A = [0,0]
	B = [shape[1]-1,0]
	C = [shape[1]-1,shape[0]-1]
	D = [0,shape[0]-1]

	# Storing input end co-ords in a single numpy array
	inpts=np.float32([A,B,C,D])

	# Initialising the new image's end co-ordinates
	newA=[]
	newB=[]
	newC=[]
	newD=[]

	# Defining the new image's co-ordinates
	newA.append(x1_coord)
	newA.append(y1_coord)
	newB.append(x2_coord)
	newB.append(y2_coord)
	newC.append(x3_coord)
	newC.append(y3_coord)
	newD.append(x4_coord)
	newD.append(y4_coord)

	# Storing output end co-ords in a single numpy array
	outpts = np.float32([newA,newB,newC,newD])

	# Finding minimum of all the x-coords and minimun of all the y-coords
	lowx=min(outpts[0][0],outpts[1][0],outpts[2][0],outpts[3][0])
	lowy=min(outpts[0][1],outpts[1][1],outpts[2][1],outpts[3][1])

	# Bringing the points to scale of (0,0)
	for i in range(len(outpts)):
		outpts[i][0]-=lowx
		outpts[i][1]-=lowy

	'''
	outpts[0][0]-=lowx
	outpts[1][0]-=lowx
	outpts[2][0]-=lowx
	outpts[3][0]-=lowx

	outpts[0][1]-=lowy
	outpts[1][1]-=lowy
	outpts[2][1]-=lowy
	outpts[3][1]-=lowy
	'''

	# Finding max of x and y-coords, in new shifted scale
	highx=max(outpts[0][0],outpts[1][0],outpts[2][0],outpts[3][0])
	highy=max(outpts[0][1],outpts[1][1],outpts[2][1],outpts[3][1])

	#newinpts = 

	# Performing the transformation of image to new co-ordinates
	M = cv2.getPerspectiveTransform(inpts,outpts)
	fimg = cv2.warpPerspective(img,M,(highx,highy))

	# Transformed image is returned
	return fimg

if __name__=="__main__":

	# Image path and reqd new image's co-ords are read
	path = sys.argv[1]
	x1_coord=int(sys.argv[2])
	y1_coord=int(sys.argv[3])
	x2_coord=int(sys.argv[4])
	y2_coord=int(sys.argv[5])
	x3_coord=int(sys.argv[6])
	y3_coord=int(sys.argv[7])
	x4_coord=int(sys.argv[8])
	y4_coord=int(sys.argv[9])

	# Transformed image 'fimg' is got
	fimg=distortimg(path,x1_coord,y1_coord,x2_coord,y2_coord,x3_coord,y3_coord,x4_coord,y4_coord)
	img=cv2.imread(path)

	cv2.imshow('Image',img)
	cv2.imshow('Fimg',fimg)
	
	# Zoomed image is saved as 'zoom_img.jpg'
	cv2.imwrite('zoom_img.jpg',fimg)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
