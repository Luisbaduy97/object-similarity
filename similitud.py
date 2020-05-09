# -*- coding: utf-8 -*-
"""
Created on Thu May  7 15:07:24 2020

@author: DELL
"""

import cv2
#import numpy as np
import os
#import matplotlib.pyplot as plt
import time

path = 'C:/Users/DELL/Desktop/NON-PROFIT-PROJECTS/SIMILITUD_ANGEL'
#im1 = 'imagen1.png'
#im2 = 'imagen2.png'

d = os.listdir(os.path.join(path))
d2 = [v for v in d if os.path.isdir(os.path.join(path, v))]

comp = os.listdir(os.path.join(path, d2[0]))
c_1 = [os.path.join(path, d2[0], v) for v in comp]

test = os.listdir(os.path.join(path, d2[1]))

t_1 = [os.path.join(path, d2[1], v) for v in test]


for i in range(len(c_1)):
    img1 = cv2.cvtColor(cv2.imread(c_1[i]),cv2.COLOR_BGR2GRAY)
    for j in range(len(t_1)):
        img2 = cv2.cvtColor(cv2.imread(os.path.join(t_1[j])),cv2.COLOR_BGR2GRAY)
        ret = cv2.matchShapes(img1,img2,1,0.0)
        print(f'{comp[i]} vs {test[j]} = {ret}')
        time.sleep(2)


#img1 = cv2.cvtColor(cv2.imread(c_1[0]),cv2.COLOR_BGR2GRAY)
#img2 = cv2.cvtColor(cv2.imread(os.path.join(path, im2)),cv2.COLOR_BGR2GRAY)


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

#ret = cv2.matchShapes(img1,img2,1,0.0)
#print(ret)







