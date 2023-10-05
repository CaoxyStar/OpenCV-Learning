import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("1.jpg", 1)
cv.imshow('image', img)
#cv.imwrite('image_save.png', img)
cv.waitKey(0)
cv.destroyAllWindows()
plt.imshow(img)
plt.show()
print(img)
