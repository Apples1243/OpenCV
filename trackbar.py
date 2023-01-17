import cv2

def update(value):
    dst = cv2.add(src, value)
    cv2.imshow('Result', dst)


src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)

cv2.namedWindow('Result')
cv2.createTrackbar('Brightness', 'Result', 0, 100, update)
update(0)
cv2.waitKey()
cv2.destroyAllWindows()
