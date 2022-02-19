from cv2 import cv2

img = cv2.imread("images/r.png", 1)
dst = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

print(img)
print(dst)


cv2.imshow('Test Image', dst)

cv2.waitKey(0)

cv2.destroyAllWindows()





