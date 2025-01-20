# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 20:47:47 2024

@author: hp
"""

import numpy as np
import cv2
b= np.zeros((256,256,3))
b=np.uint8(b)
for i in range(128):
    for j in range(i):
        b[i][255-j][2]=255
        b[i][255-j][0]=255
for i in range(128):
    for j in range(i):
        b[255-i][j][0]=230
        b[255-i][j][1]=230
        b[255-i][255-j][2]=250
        

for j in range(127,-1,-1):
    for  i in range(j):
        b[255-i][j][0]=225
        b[255-i][j][1]=225
        b[255-i][j][2]=225
        
for j in range(127,-1,-1):
    for i in range(j):
        b[i][255-j][1]= 240
        b[i][255-j][2]= 230
        b[255-i][255-j][1]=225
        
cv2.imwrite("imagegen.png",b)



