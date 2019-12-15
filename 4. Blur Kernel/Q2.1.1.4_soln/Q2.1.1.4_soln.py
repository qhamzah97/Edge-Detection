import cv2
import numpy as np
from scipy import signal

img = cv2.imread('bears.jpg',0)

def spatial_filter(img,h):
    print(img)
    img = img.astype(float)
    print(img)
    img = signal.convolve2d(img,h, boundary = 'symm', mode ='same')
    return img

filter = np.array([[1, 4, 7, 4, 1],
                [4, 20, 33, 20, 4],
                [7, 33, 55, 33, 7],
                [4, 20, 33, 20, 4],
                [1, 4, 7, 4, 1]])
filter = filter * (1/331)

spatial_filter = spatial_filter(img, filter)
cv2.imwrite('bears_new.jpg', spatial_filter)
