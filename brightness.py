import cv2

# source (소스)
src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)
# 검정색(=0), 흰색(=255)


# destination
# dst1 = src + 100    # <----- 픽셀값이 255보다 큰 경우 오류 발생
# dst2 = src - 100    # <----- 픽셀값이 0보다 작은 경우 오류 발생

dst1 = cv2.add(src, 100)     # 더하기 (밝게)
dst2 = cv2.subtract(src, 100)    # 빼기 (어둡게)

cv2.imshow('source', src)
cv2.imshow('add', dst1)
cv2.imshow('subtract', dst2)
cv2.waitKey()
cv2.destroyAllWindows()
