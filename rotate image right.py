import cv2
import numpy as np

img = cv2.imread("image.jpg")
img= cv2.resize(img,(500,500))
cv2.imshow("Original image", img)


def rotate_right(img):
    img_transpose = img.transpose()
    channel, height, width = np.shape(img_transpose)
    new_img = np.zeros((height, width, channel), dtype=np.uint8)

    for i in range(height - 1):
        for j in range(width - 1):
            for k in range(channel):
                new_img[i, j, k] = img_transpose[k, i, width - j - 1]


    cv2.imshow("Rotated image", new_img)
    cv2.waitKey(0)


rotate_right(img)