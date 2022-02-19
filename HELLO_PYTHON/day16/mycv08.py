from cv2 import cv2

img = cv2.imread("images/sungyun.jfif", 1)

cv2.imwrite('images/iu.jpg', img)

cv2.imshow('Test Image', img)

cv2.waitKey(0)

cv2.destroyAllWindows()





