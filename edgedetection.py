# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 14:31:14 2024

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



I=cv2.imread("lena.jpeg",0)
kernel=np.array([[1,0,-1],[2,0,-2],[1,0,-1]])
Ix= convolve_image(I, kernel)
cv2.imwrite("Temp_Ix.jpeg",Ix)

kernel=np.array([[1,2,1],[0,0,0],[-1,-2,-1]])
Iy= convolve_image(I, kernel)
cv2.imwrite("Temp_Iy.jpeg",Iy)

Ix= np.float32(Ix)
Iy= np.float32(Iy)
Grad= np.sqrt(Ix**2+Iy**2)
Grad= Grad/np.max(Grad)
Grad= Grad*255
Grad=np.uint8(Grad)
cv2.imwrite("Gradient_imagelena.jpeg", Grad)

