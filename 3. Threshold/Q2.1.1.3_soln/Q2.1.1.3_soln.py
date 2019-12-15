import numpy as np 
import cv2

T = float(input("Give 'T' either 0 or 1 input: \n"))
print(T)
while T<0.0 or T>1.0:
    print("invalid input choose another value for B")
    T = float(input("Give 'T' either 0 or 1 input:"))
    print(T)


def image_thresholding(image, T):
    img = cv2.imread(image,0)
    img = np.array(img)
    print(img)
    img = img.astype(float)
    T_img=img/255
    print(T_img)
    for x in range(len(img)):
        for y in range(len(img[x])):
            if(T_img[x][y]<T):
                T_img[x][y] =0  # if less than T = 0
            img[x][y] = 1   # if greater than or equal to t  =1
    cv2.imshow('image', T_img)
    cv2.waitKey(1)
   
    return(T_img)

img =image_thresholding('threshold-test.png',T)