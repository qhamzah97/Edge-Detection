import cv2
import numpy as np
from scipy import signal
import math

print("Choose one of the following Dereivative filters to apply to your image\n")
print("If you are unawae of what each filter does type the command 'help' for information on each filter\n")
Selector = str(input(" Select A for : Central Difference Filter \n Select B for : Forward Difference Filter \n Select C for : Prewitt Filter \n Select D for : Sobel Filter \n Select help for information on the filters\n"))
while ((Selector != 'A') and  (Selector != "B") and (Selector != "C") and (Selector != "D") and (Selector != "help")):
    print(" INVALID INPUT \n Please input a valid option\n")
    Selector = str(input(" Select A for : Central Difference Filter \n Select B for : Forward Difference Filter \n Select C for : Prewitt Filter \n Select D for : Sobel Filter \n Select help for information on the filters\n"))


def Kernal_Options(S):
     
    CD = np.array([[1, 0, -1]])

    FD = np.array([[0, 1, -1]])

    Pr = np.array([[1, 0, -1],
          [1, 0, -1],
          [1, 0, -1]])

    So = np.array([[1, 0, -1],
          [2, 0, -2],
          [1, 0, -1]])

    if (S == "A"):
        print(CD)
        return(CD)
    elif (S == "B"):
        print(FD)
        return(FD)
    elif(S == "C"):
       print(Pr[0])
       print(Pr[1])
       print(Pr[2])
       return(Pr)
    elif(S == "D"):
       print(So[0])
       print(So[1])
       print(So[2])
       return(So)
    elif(S == "help"):

        print("The purpose of the Centeral Difference Kernal is: \n" )
        print("The purpose of the Forward Difference Kernal is: \n" )
        print("The purpose of the Prewitt Kernal is: \n" )
        print("The purpose of the Sobel Difference Kernal is: \n" )
        
        print("Choose one of the following Dereivative filters to apply to your image\n")
        print("If you are unawae of what each filter does type the command 'help' for information on each filter\n")
        print("Restart the program and select the filter you would like to apply")
        Selector2 = str(input(" Select A for : Central Difference Filter \n Select B for : Forward Difference Filter \n Select C for : Prewitt Filter \n Select D for : Sobel Filter \n Select help for information on the filters \n"))
        while ((Selector2 != 'A') and  (Selector2 != "B") and (Selector2 != "C") and (Selector2 != "D") and (Selector2 != "help")):
            print(" INVALID INPUT \n Please input a valid option\n")
            Selector2 = str(input(" Select A for : Central Difference Filter \n Select B for : Forward Difference Filter \n Select C for : Prewitt Filter \n Select D for : Sobel Filter \n Select help for information on the filters \n"))
        return (Kernal_Options(Selector2))
    return 

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
    img_x = spatial_filter(img, mask_X)
    cv2.imwrite('Ix(x,y).jpg', img_x)
    print("Spatial Filter for horizontal graident has been created \n")
    img_y = spatial_filter(img, mask_Y)
    print("Spatial Filter for vertical graident has been created \n")
    cv2.imwrite('Iy(x,y).jpg', img_y)
    
    img_X = np.array(img_x)
    img_Y = np.array(img_y)
    rows_x, columns_x = img_X.shape[:2]
    rows_y, columns_y = img_Y.shape[:2]
#    if rows_x != rows_y:
#        diff_row = abs(rows_x - rows_y)
#        if rows_x > rows_y:
#            con = np.zeros([diff_row, columns_y])
#            img_Y = np.append(img_Y, con)
#        else:
#            con = np.zeros([diff_row, columns_x])
#            img_X = np.append(img_X, con)
#    if columns_x != columns_y:
#        diff_columns = abs(columns_x - columns_y)
#        if columns_x > columns_y:
#            con = np.zeros([rows_y, diff_columns])
#            img_Y = np.append(img_Y, con)
#        else:
#            con = np.zeros([rows_x, diff_columns])
#            img_X = np.append(img_X, con)
    
    
    rows_x, columns_x = img_X.shape[:2]
    rows_y, columns_y = img_Y.shape[:2]
    if rows_x != rows_y:
        diff_row = abs(rows_x - rows_y)
        if rows_x > rows_y:
            np.pad(img_Y, ((0,0),(math.floor(diff_row/2),math.ceil(diff_row/2))))
        else:
            np.pad(img_X, ((0,0),(math.floor(diff_row/2),math.ceil(diff_row/2))))
    if columns_x != columns_y:
        diff_columns = abs(columns_x - columns_y)
        if columns_x > columns_y:
            np.pad(img_Y, ((math.floor(diff_columns/2),math.ceil(diff_columns/2)),(0,0)))
        else:
            np.pad(img_Y, ((math.floor(diff_columns/2),math.ceil(diff_columns/2)),(0,0)))
    print(img_X.shape)
    print(img_Y.shape)
    Img_Gradient = img_X
    rows, columns = Img_Gradient.shape[:2]
    print(Img_Gradient.shape)
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
    cv2.imshow('Threshold ImageX',Threshold_Image_X)
    cv2.waitKey(0)

    Threshold_Image_Y = image_thresholding(NMS_Image_Y, T)
    print("Threshold Image for vertical gradient has been created \n")
    cv2.imshow('Threshold ImageY',Threshold_Image_Y)
    cv2.waitKey(0)

    E = Threshold_Image_X
    rows, columns = Threshold_Image_X.shape[:2]
    for i in range (0, rows):
        for j in range (0, columns):
            if Threshold_Image_X[i][j]==1 or Threshold_Image_Y[i][j]==1:
                E[i][j] = 1
    print("Edge Map has been created \n")
    cv2.imshow('Edge Map', E)
    cv2.waitKey(0)

g_img = cv2.imread('bears.jpg', 0)
mask = Kernal_Options(Selector)

edge_detector(g_img, mask, 0.5, 5)
