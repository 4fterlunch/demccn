import numpy as np
import cv2
import os
#from matplotlib import pyplot as plt

dir = os.path.dirname(__file__)

img = cv2.imread(os.path.join(dir,'img_test.jpg'), 0)

# apply theshold

thresh = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
                                        cv2.THRESH_BINARY,11,2)




cv2.imshow('image', thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
