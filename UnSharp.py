import cv2

# 원본 영상
src = cv2.imread('rose.bmp', cv2.IMREAD_GRAYSCALE)

sigma = 1

# 언샤프 영상 (= 부드러워진 영상)
blurred = cv2.GaussianBlur(src, (0, 0), sigma)

alpha = 5.0

dst = cv2.addWeighted(src, 1 + alpha, blurred, -alpha, 0.0)

cv2.imshow('Org', src)
cv2.imshow('UnSharp', blurred)
cv2.imshow('Sharp', dst)
cv2.waitKey()
cv2.destroyAllWindows()
