import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('./HDR.jpg', cv2.IMREAD_GRAYSCALE)
plt.subplot(121),plt.imshow(img, cmap='gray')
plt.title("Original Image")
plt.axis('off')
th1 = cv2.equalizeHist(img)

plt.subplot(122),plt.imshow(th1,'gray')
plt.title("Histogram-Equalized Image")
plt.xticks([]), plt.yticks([])

plt.suptitle("Histogram Equalization")
plt.show()
