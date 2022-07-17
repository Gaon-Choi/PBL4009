import numpy as np
import cv2
from matplotlib import pyplot as plt

cap = cv2.VideoCapture('./pedestrians.mp4')

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))

fgb = cv2.createBackgroundSubtractorMOG2()

while(1):
    ret, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    fgmask = fgb.apply(frame)
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)

    plt.subplot(121)
    plt.imshow(frame, cmap='gray')
    plt.title("Original Image")

    plt.subplot(122)
    plt.imshow(fgmask, cmap='gray')
    plt.title("After BS processing")
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    plt.show()

cap.release()
cv2.destroyAllWindows()
