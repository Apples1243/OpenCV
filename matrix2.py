import cv2

img1 = cv2.imread('lenna.bmp', cv2.IMREAD_COLOR)

img2 = img1[200:400, 200:400, :]


cv2.imshow('girl', img1)
cv2.imshow('face', img2)
cv2.waitKey()
cv2.destroyAllWindows()
