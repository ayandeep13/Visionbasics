# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 08:35:04 2024

@author: hp
"""

import numpy as np
import cv2

def convolve_image(I, kernel):
    s = I.shape
    kernel_size = 3
    new_image = np.uint8(np.zeros((s[0] - kernel_size + 1, s[1] - kernel_size + 1)))

    for i in range(s[0] - kernel_size + 1):
        for j in range(s[1] - kernel_size + 1):
            part_image = I[i:i + kernel_size, j:j + kernel_size]
            prod = part_image * kernel
            intensity = np.sum(prod)
            new_image[i, j] = intensity

    return new_image

def apply_hysteresis(grad, low_threshold, high_threshold):
    strong = 255
    weak = 75

    strong_i, strong_j = np.where(grad >= high_threshold)
    weak_i, weak_j = np.where((grad <= high_threshold) & (grad >= low_threshold))

    grad_hysteresis = np.zeros_like(grad, dtype=np.uint8)
    grad_hysteresis[strong_i, strong_j] = strong
    grad_hysteresis[weak_i, weak_j] = weak

    M, N = grad.shape
    for i in range(1, M - 1):
        for j in range(1, N - 1):
            if grad_hysteresis[i, j] == weak:
                if ((grad_hysteresis[i + 1, j - 1] == strong) or (grad_hysteresis[i + 1, j] == strong) or
                    (grad_hysteresis[i + 1, j + 1] == strong) or (grad_hysteresis[i, j - 1] == strong) or
                    (grad_hysteresis[i, j + 1] == strong) or (grad_hysteresis[i - 1, j - 1] == strong) or
                    (grad_hysteresis[i - 1, j] == strong) or (grad_hysteresis[i - 1, j + 1] == strong)):
                    grad_hysteresis[i, j] = strong
                else:
                    grad_hysteresis[i, j] = 0

    return grad_hysteresis


I = cv2.imread("lena2.png", 0)

kernel_x = np.array([[1, 0, -1], [2, 0, -2], [1, 0, -1]])
kernel_y = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])

Ix = convolve_image(I, kernel_x)
Iy = convolve_image(I, kernel_y)

cv2.imwrite("Temp_Ix.png", Ix)
cv2.imwrite("Temp_Iy.png", Iy)

Ix = np.float32(Ix)
Iy = np.float32(Iy)
Grad = np.sqrt(Ix**2 + Iy**2)
Grad = Grad / np.max(Grad)
Grad = Grad * 255
Grad = np.uint8(Grad)


low_threshold = 50
high_threshold = 100
Grad_hysteresis = apply_hysteresis(Grad, low_threshold, high_threshold)

cv2.imwrite("Gradient_image_lena.png", Grad)
cv2.imwrite("Gradient_hysteresis_image_lena.png", Grad_hysteresis)
