from cv2 import cv2

img = cv2.imread("images/sungyun.jfif", 1)

(w,h) = img.shape[:2]
print(w, h)

# dst = cv2.resize(img, dsize=(w * 2, h * 2), interpolation=cv2.INTER_AREA)
dst = cv2.resize(img, dsize=(0, 0), fx=2, fy=2, interpolation=cv2.INTER_AREA)

cv2.imshow('Test Image', dst)

cv2.waitKey(0)

cv2.destroyAllWindows()





