import cv2

# haarcascade 불러오기
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# 이미지 불러오기
img = cv2.imread('images/sungyun.jfif', cv2.IMREAD_COLOR)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img2 = cv2.imread('images/pengsu.png', cv2.COLOR_BGR2GRAY)

ret, mask = cv2.threshold(img2, 100, 255, cv2.THRESH_BINARY)


mask_inv = cv2.bitwise_not(mask)

roi = "";

# 얼굴 찾기
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    
    roi = img[x : x + w, y : y + h]
    
    im2_fg = cv2.bitwise_and(img, img2, mask=mask)
    cv2.imshow('img_fg', im2_fg)
    
    
    
    # 눈 찾기
    # roi_color = img[y:y + h, x:x + w]
    # roi_gray = gray[y:y + h, x:x + w]
    # eyes = eye_cascade.detectMultiScale(roi_gray)
    # for (ex, ey, ew, eh) in eyes:
    #     cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)



# 영상 출력
cv2.imshow('image', img)

key = cv2.waitKey(0)
cv2.destroyAllWindows()