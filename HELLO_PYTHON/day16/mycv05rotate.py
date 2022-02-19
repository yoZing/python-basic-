from cv2 import cv2

img = cv2.imread("images/sungyun.jfif", 1)


(h, w) = img.shape[:2]
(cX, cY) = (w /2, h / 2)

rot_info = cv2.getRotationMatrix2D((cX, cY), 23, 1.0)
img_45 = cv2.warpAffine(img, rot_info, (w, h))



cv2.imshow('Test Image', img_45)

cv2.waitKey(0)

cv2.destroyAllWindows()





