import numpy as np
import cv2
#from matplotlib import pyplot as plt

img = cv2.imread('img_test.jpg', 0)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
