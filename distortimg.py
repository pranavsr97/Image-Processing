import cv2
import numpy as np
import sys

path = sys.argv[1]
img=cv2.imread(path)

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

newA.append(int(sys.argv[2]))
newA.append(int(sys.argv[3]))
newB.append(int(sys.argv[4]))
newB.append(int(sys.argv[5]))
newC.append(int(sys.argv[6]))
newC.append(int(sys.argv[7]))
newD.append(int(sys.argv[8]))
newD.append(int(sys.argv[9]))

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

cv2.imshow('Image',img)
cv2.imshow('Fimg',fimg)
cv2.waitKey(0)
cv2.destroyAllWindows()