import sys 
import numpy as np
import cv2
from scipy import misc
from scipy.ndimage import convolve
from scipy import signal 


#2.1.1 #1

img = cv2.imread('bears.jpg',0)
h,w  = 3,3
filter = [[0 for x in range(h)] for y in range(w)]
filter[0][0] = -1.0
filter[0][1] = -1.0
filter[0][2] = -1.0
filter[1][0] = -1.0
filter[1][1] = 8
filter[1][2] = -1.0
filter[2][0] = -1.0
filter[2][1] = -1.0
filter[2][2] = -1.0

def spatial_filter(img,h):
    print(img)
    img = img.astype(float)
    print(img)
    img = signal.convolve2d(img,h, boundary = 'symm', mode ='same')

    return img;

spatial_filter = spatial_filter(img, filter)
cv2.imwrite('bears_new.jpg', spatial_filter)
