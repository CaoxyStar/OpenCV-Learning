import cv2

cv2.namedWindow('rgb_1', cv2.WINDOW_NORMAL)
cv2.namedWindow('rgb_2', cv2.WINDOW_NORMAL)
cv2.namedWindow('rgb_3', cv2.WINDOW_NORMAL)
url_1 = "rtsp://admin:@192.168.1.4"
url_2 = "rtsp://admin:@192.168.1.5"
url_3 = "rtsp://admin:@192.168.1.6"
cap_1 = cv2.VideoCapture(url_1)
cap_2 = cv2.VideoCapture(url_2)
cap_3 = cv2.VideoCapture(url_3)

ret_1, frame_1 = cap_1.read()
ret_2, frame_2 = cap_2.read()
ret_3, frame_3 = cap_3.read()

cap_1.set(cv2.CAP_PROP_FPS, 5)
print(cap_1.get(cv2.CAP_PROP_FPS))

while ret_1 and ret_2 and ret_3:
    ret_1, frame_1 = cap_1.read()
    ret_2, frame_2 = cap_2.read()
    ret_3, frame_3 = cap_3.read()
    cv2.imshow("rgb_1", frame_1)
    #cv2.imshow("rgb_2", frame_2)
    #cv2.imshow("rgb_3", frame_3)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap_1.release()
cap_2.release()
cap_3.release()
cv2.destroyAllWindows()
