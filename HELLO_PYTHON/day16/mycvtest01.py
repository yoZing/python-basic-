from cv2 import cv2

img = cv2.imread("images/sungyun.jfif", 1)

iu = img[50:150, 110:170].copy()

iu2 = cv2.imwrite('images/iu2.jpg', iu)


cv2.imshow('Test Image', img)

cv2.waitKey(0)

cv2.destroyAllWindows()





