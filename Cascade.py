import cv2

img = cv2.imread('kids.png', cv2.IMREAD_COLOR)

# Cascade + Classifier(=분류기)
# Classify : v. 분류하다.
# Classification : n. 분류
# Classifier : 분류자, 분류기

face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_classifier = cv2.CascadeClassifier('haarcascade_eye.xml')

faces = face_classifier.detectMultiScale(img)

for (x1, y1, w1, h1) in faces:
    cv2.rectangle(img, (x1, y1), (x1+w1, y1+h1), (255, 0, 0), 5)

    faceROI = img[y1:(y1+h1), x1:(x1+w1)]   # 얼굴 영역
    # ROI (= Region of Interest, 관심 영역)
    eyes = eye_classifier.detectMultiScale(faceROI)

    for (x2, y2, w2, h2) in eyes:
        center = (int(x2 + w2 / 2), int(y2 + h2 / 2))
        cv2.circle(faceROI, center, int(w2 / 2), (0, 0, 255), 3, cv2.LINE_AA)

cv2.imshow('Kids', img)
cv2.waitKey()
cv2.destroyAllWindows()
