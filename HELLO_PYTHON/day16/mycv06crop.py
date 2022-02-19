from cv2 import cv2

img = cv2.imread("images/sungyun.jfif", 1)

print(img.shape)

dst = img[50:150, 110:170].copy()


cv2.imshow('Test Image', dst)

cv2.waitKey(0)

cv2.destroyAllWindows()





