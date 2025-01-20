# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 20:35:26 2024

@author: hp
"""

import cv2
import numpy as np
I= cv2.imread("leaf.png",0)
s= I.shape
negative_image = np.zeros(s, dtype=np.uint8)
for i in range(s[0]):
    for j in range(s[1]):
        negative_image[i, j] = 255 - I[i, j]

cv2.imwrite('negative_leaf.png', negative_image)
