import cv2 as cv
from matplotlib import pyplot as plt

gray = cv.imread('./dog.jpg', cv.IMREAD_GRAYSCALE)
plt.subplot(121),plt.imshow(gray, cmap='gray')
plt.title("Original Image")
plt.axis('off')

ddepth = cv.CV_16S; scale = 1; delta = 0
grad_x = cv.Sobel(gray, ddepth, 1, 0, ksize=3, scale=scale, delta=delta, borderType=cv.BORDER_DEFAULT)
# Gradient-Y
# grad_y = cv.Scharr(gray,ddepth,0,1)
grad_y = cv.Sobel(gray, ddepth, 0, 1, ksize=3, scale=scale, delta=delta, borderType=cv.BORDER_DEFAULT)

abs_grad_x = cv.convertScaleAbs(grad_x)
abs_grad_y = cv.convertScaleAbs(grad_y)

grad = cv.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)
plt.subplot(122),plt.imshow(grad, cmap='gray')
plt.title("Sobel_filter Applied Image")

plt.show()