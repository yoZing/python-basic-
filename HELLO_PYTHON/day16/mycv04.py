from cv2 import cv2

img = cv2.imread("images/sungyun.jfif", 1)

img_flip = cv2.flip(img, 0)

img_rotate = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

print(img)
print(img_flip)
print(img_rotate)

cv2.imshow('Test Image', img)

cv2.waitKey(0)

cv2.destroyAllWindows()





