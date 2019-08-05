import numpy as np
import cv2
import os
#from matplotlib import pyplot as plt

dir = os.path.dirname(__file__)

img = cv2.imread(os.path.join(dir,'img_test.jpg'), 0)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
