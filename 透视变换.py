import cv2
import numpy as np

img = cv2.imread('12.jpg')
img_resize = cv2.resize(img, None, fx=2, fy=2)
img_resize2 = cv2.resize(img, (960, 300))

#平移
rows, cols, channels = img.shape
M = np.float32([[1, 0, 700], [0, 1, 400]])
dst = cv2.warpAffine(img, M, (cols, rows))
#旋转
M_rotation = cv2.getRotationMatrix2D(((cols-1)/2, (rows-1)/2), 90, 1)
dst2 =cv2.warpAffine(img, M_rotation, (cols, rows))
#透视（三维，仿射变换为平面变换）
pts1 = np.float32([[810, 480], [785, 740], [1200, 880], [1235, 500]])
pts2 = np.float32([[360, 140], [360, 940], [640, 940], [640, 140]])
M_per = cv2.getPerspectiveTransform(pts1, pts2)
dst3 = cv2.warpPerspective(img, M_per, (1920, 1080))

cv2.namedWindow('img', cv2.WINDOW_NORMAL)
cv2.imshow("img", dst3)
cv2.waitKey(0)
cv2.destroyAllWindows()