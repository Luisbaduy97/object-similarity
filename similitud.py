# -*- coding: utf-8 -*-
"""
Created on Thu May  7 15:07:24 2020

@author: DELL
"""

import cv2
#import numpy as np
import os
#import matplotlib.pyplot as plt

path = 'C:/Users/DELL/Desktop/NON-PROFIT-PROJECTS/SIMILITUD_ANGEL'
im1 = 'imagen1.png'
im2 = 'imagen2.png'

img1 = cv2.cvtColor(cv2.imread(os.path.join(path, im1)),cv2.COLOR_BGR2GRAY)
img2 = cv2.cvtColor(cv2.imread(os.path.join(path, im2)),cv2.COLOR_BGR2GRAY)


## To visualize images
# plt.figure(1)
# plt.subplot(1,2,1)
# plt.imshow(img1, 'gray')
# plt.subplot(1,2,2)
# plt.imshow(img2, 'gray')


#ret, thresh = cv2.threshold(img1, 127, 255,0)
#ret, thresh2 = cv2.threshold(img2, 127, 255,0)


#contours,hierarchy = cv2.findContours(thresh,2,1)
#cnt1 = contours[0]
#contours,hierarchy = cv2.findContours(thresh2,2,1)
#cnt2 = contours[0]

ret = cv2.matchShapes(img1,img2,1,0.0)
print(ret)







