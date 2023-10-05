import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
cv2.line(img, (0, 0), (511, 511), (0, 255, 0), 5)
cv2.rectangle(img, (100, 100), (400, 400), (255, 0, 0), 5)
cv2.circle(img, (255, 255), 50, (0, 0, 255), 10)
cv2.ellipse(img, (255, 255), (100, 50), 45, 0, 360, (100, 100, 100), 3)
cv2.putText(img, 'Stephen Curry', (100, 400), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 4, cv2.LINE_AA)
pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
cv2.polylines(img, [pts], True, (0, 255, 255))
cv2.imshow("img", img)
cv2.imwrite("img_plot.jpg", img)
cv2.waitKey(0)
cv2.destroyAllWindows()