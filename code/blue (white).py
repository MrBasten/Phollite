import cv2
import numpy as np

hsv_min = np.array((90, 23, 0), np.uint8)
hsv_max = np.array((144, 255, 255), np.uint8)

img = cv2.imread(r'C:\Users\HP\Desktop\practic\ng.png')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
thresh = cv2.inRange(hsv, hsv_min, hsv_max)

cv2.imshow('result', thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
