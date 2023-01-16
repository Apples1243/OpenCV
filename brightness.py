import cv2

# source (소스)
src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)
# 검정색(=0), 흰색(=255)


# destination
dst = cv2.add(src, 100)

cv2.imshow('source', src)
cv2.imshow('destination', dst)
cv2.waitKey()
cv2.destroyAllWindows()