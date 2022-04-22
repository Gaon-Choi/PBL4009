import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('./dog.jpg', cv2.IMREAD_GRAYSCALE)
plt.subplot(121),plt.imshow(img, cmap='gray')
plt.title("Original Image")
plt.axis('off')
ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

plt.subplot(122),plt.imshow(th1,'gray')
plt.title("Threshold Image")
plt.xticks([]), plt.yticks([])

plt.suptitle("Image Thresholding")
plt.show()
