import cv2
import numpy as np
# import matplotlib.pyplot as plt


def calcGrayHist(img):
   channels = [0]
   histSize = [256]
   histRange = [0, 256]

   h = cv2.calcHist([img], channels, None, histSize, histRange)

   return h


def getGrayHistImage(h):
    imgHist = np.full((100, 256), 0, dtype=np.uint8)
    for x in range(256):
        p1 = (x, 100)     # point의 첫 글자
        p2 = (x, 100 - int((h[x, 0] / np.max(h)) * 100))
        cv2.line(imgHist, p1, p2, 255) # 검정색 선을 그려라

    return imgHist


src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)
h = calcGrayHist(src)

cv2.imshow('Image', src)
cv2.imshow('Histogram', getGrayHistImage(h))
cv2.waitKey()
cv2.destroyAllWindows()

# print(h.shape)

# plt.bar(range(256), np.transpose(h)[0])
# plt.grid(True)
# plt.show()
