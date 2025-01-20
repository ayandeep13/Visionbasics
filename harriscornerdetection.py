# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 15:06:06 2024

@author: hp
"""

import numpy as np
import cv2
def convolve_image(I,kernel):
    s=I.shape
    kernel_size=3
    new_image= np.uint8(np.zeros((s[0]-kernel_size+1,s[1]-kernel_size+1)))
    
    for i in range(s[0]-kernel_size+1):
        for j in range(s[1]-kernel_size+1):
            part_image= I[i:i+kernel_size,j:j+kernel_size]
            #print(part_image.shape)
            prod= part_image*kernel
            intensity=np.sum(prod)
            new_image[i,j]= intensity
    
    return new_image



I=cv2.imread("lena2.png",0)
I=np.float32(I)
kernel_x= np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
Ix= convolve_image(I, kernel_x)
kernel_y= np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
Iy= convolve_image(I, kernel_y)
Ix=np.float32(Ix)
Iy=np.float32(Iy)
Ixx=Ix*Ix
Iyy=Iy*Iy
Ixy=Ix*Iy
Ixx=np.float32(Ixx)
Iyy=np.float32(Iyy)
Ixy=np.float32(Ixy)
det=Ixx*Iyy- Ixy**2
R=det - 0.6*(Ixx+Iyy)**2
R=(R-np.min(R))/(np.max(R)- np.min(R))
R*=255
s3=R.shape
for i in range(s3[0]):
    for j in range(s3[1]):
        if (R[i,j]<150):
            R[i,j]=0
        else:
            R[i,j]=255
                   
cv2.imwrite("lenacorner.png",R)

