import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('dog.jpg')
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
edges = cv.Canny(img, 100, 200)
plt.subplot(121),plt.imshow(img)
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges)
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.suptitle("Canny Edge Detection")
plt.show()