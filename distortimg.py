import cv2
import numpy as np
import sys

def distortimg(imgpath,x1_coord,y1_coord,x2_coord,y2_coord,x3_coord,y3_coord,x4_coord,y4_coord):

	img=cv2.imread(imgpath)

	shape = img.shape

	print shape

	A = [0,0]
	B = [shape[1]-1,0]
	C = [shape[1]-1,shape[0]-1]
	D = [0,shape[0]-1]

	inpts=np.float32([A,B,C,D])

	newA=[]
	newB=[]
	newC=[]
	newD=[]

	newA.append(x1_coord)
	newA.append(y1_coord)
	newB.append(x2_coord)
	newB.append(y2_coord)
	newC.append(x3_coord)
	newC.append(y3_coord)
	newD.append(x4_coord)
	newD.append(y4_coord)

	outpts = np.float32([newA,newB,newC,newD])

	lowx=min(outpts[0][0],outpts[1][0],outpts[2][0],outpts[3][0])
	lowy=min(outpts[0][1],outpts[1][1],outpts[2][1],outpts[3][1])

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

	highx=max(outpts[0][0],outpts[1][0],outpts[2][0],outpts[3][0])
	highy=max(outpts[0][1],outpts[1][1],outpts[2][1],outpts[3][1])

	#newinpts = 

	M = cv2.getPerspectiveTransform(inpts,outpts)
	fimg = cv2.warpPerspective(img,M,(highx,highy))
	return fimg

if __name__=="__main__":

	path = sys.argv[1]
	x1_coord=int(sys.argv[2])
	y1_coord=int(sys.argv[3])
	x2_coord=int(sys.argv[4])
	y2_coord=int(sys.argv[5])
	x3_coord=int(sys.argv[6])
	y3_coord=int(sys.argv[7])
	x4_coord=int(sys.argv[8])
	y4_coord=int(sys.argv[9])

	fimg=distortimg(path,x1_coord,y1_coord,x2_coord,y2_coord,x3_coord,y3_coord,x4_coord,y4_coord)
	img=cv2.imread(path)
	cv2.imshow('Image',img)
	cv2.imshow('Fimg',fimg)
	cv2.waitKey(0)
	cv2.destroyAllWindows()