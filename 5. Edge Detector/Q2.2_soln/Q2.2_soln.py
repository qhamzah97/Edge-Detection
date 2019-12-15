import cv2
import numpy as np
from scipy import signal
import math

def spatial_filter(img,h):
    img = img.astype(float)
    img = signal.convolve2d(img,h)
    return img;

def non_max_suppress(image, H, W):
    #img = cv2.imread(image, 0)
    img = image.astype(float)
    new_image = np.zeros(img.shape)
    range_w = range(-math.floor(W/2), math.ceil(W/2))
    range_h = range(-math.floor(H/2), math.ceil(H/2))
    for i in range(len(img)):
        for j in range(len(img[i])):
            max = 0
            for x in range_h:
                for y in range_w:
                    if (i+x) >= 0 and (i+x) < len(img) and (j+y) >=0 and (j+y) < len(img[i]):
                        if img[i+x][j+y] > max:
                            max = img[i+x][j+y]
            if img[i][j] < max:
                new_image[i][j] = 0
            else:
                new_image[i][j] = img[i][j]
    return new_image

def image_thresholding(image, T):
    #img = cv2.imread(image,0)
    img = np.array(image)
    #img = img.astype(float)
    T_img=img/255
    for x in range(len(img)):
        for y in range(len(img[x])):
            if(T_img[x][y]<T):
                T_img[x][y] =0  # if less than T = 0
            img[x][y] = 1   # if greater than or equal to t  =1
    return(T_img)

def edge_detector(img, H, T, wndsz):
    mask_X = H
    mask_Y = H.transpose()
    img_X = spatial_filter(img, mask_X)
    cv2.imwrite('Ix(x,y).jpg', img_X)
    print("Spatial Filter for horizontal graident has been created \n")
    img_Y = spatial_filter(img, mask_Y)
    print("Spatial Filter for vertical graident has been created \n")
    cv2.imwrite('Iy(x,y).jpg', img_Y)
    
    Img_Gradient = img_X
    rows, columns = img_X.shape[:2]
    for i in range (0, rows):
        for j in range (0, columns):
            Img_Gradient[i][j] = math.sqrt(math.pow(img_X[i][j],2) + math.pow(img_Y[i][j],2))
    print("Image Gradient has been created \n")
    cv2.imwrite('Image Gradient.jpg', Img_Gradient)

    NMS_Image_X = non_max_suppress(Img_Gradient, 1, wndsz)
    print("NMS Image for horizontal gradient has been created \n")
    cv2.imwrite('NMS Image X.jpg', NMS_Image_X)   
    NMS_Image_Y = non_max_suppress(Img_Gradient, wndsz, 1)
    print("NMS Image for vertical gradient has been created \n")
    cv2.imwrite('NMS Image Y.jpg', NMS_Image_Y)

    Threshold_Image_X = image_thresholding(NMS_Image_X, T)
    print("Threshold Image for horizontal gradient has been created \n")
    cv2.imwrite('Threshold Image X.jpg', Threshold_Image_X)
    cv2.imshow('Threshold ImageX',Threshold_Image_X)
    cv2.waitKey(0)

    Threshold_Image_Y = image_thresholding(NMS_Image_Y, T)
    print("Threshold Image for vertical gradient has been created \n")
    cv2.imwrite('Threshold Image Y.jpg', Threshold_Image_Y)
    cv2.imshow('Threshold ImageY',Threshold_Image_Y)
    cv2.waitKey(0)

    E = Threshold_Image_X
    rows, columns = Threshold_Image_X.shape[:2]
    for i in range (0, rows):
        for j in range (0, columns):
            if Threshold_Image_X[i][j]==1 or Threshold_Image_Y[i][j]==1:
                E[i][j] = 1
    print("Edge Map has been created \n")
    cv2.imwrite('Edge Map.jpg', E)
    cv2.imshow('Edge Map', E)
    cv2.waitKey(0)

g_img = cv2.imread('bears.jpg', 0)
mask = np.array([[1,0,-1],
                 [2,0,-2],
                 [1,0,-1]])
edge_detector(g_img, mask, 0.5, 5)
