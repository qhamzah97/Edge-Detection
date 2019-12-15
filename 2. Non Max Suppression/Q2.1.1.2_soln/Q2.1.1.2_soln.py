import cv2
import math
import numpy as np

def non_max_suppress(image, H, W):
    max = 0
    img = cv2.imread(image, 0)
    img = img.astype(float)
    new_image = np.zeros(img.shape)

    range_w = range(-math.floor(W/2), math.ceil(W/2))
    range_h = range(-math.floor(H/2), math.ceil(H/2))
    for i in range(len(img)):
        for j in range(len(img[i])):
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

out = non_max_suppress('nms-test.png', 5, 5)
cv2.imwrite('nms-result.png', out)