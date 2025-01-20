# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 08:47:42 2024

@author: hp
"""
import cv2
import numpy as np

I = cv2.imread("lena.jpeg", 0)

kernel = np.array([[1, 2, 1], 
                   [2, 4, 2], 
                   [1, 2, 1]],) 
kernel= kernel/16
rows, cols = I.shape
blurred_image = np.zeros((rows-2, cols-2))
for i in range(1, rows-1):
    for j in range(1, cols-1):
        region = I[i-1:i+2, j-1:j+2]    
        blurred_image[i-1, j-1] = np.sum(region * kernel)

blurred_image = blurred_image.astype(np.uint8)

cv2.imwrite("blurredlena.png", blurred_image)
