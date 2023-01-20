import cv2
import numpy as np

img = cv2.imread('circuit.bmp', cv2.IMREAD_COLOR)
tmp = cv2.imread('crystal.bmp', cv2.IMREAD_COLOR)

print(img.shape)

img = img + (50, 50, 50)    # (Blue, Green, Red)

noise = np.zeros(img.shape, np.int32)
cv2.randn(noise, 0, 10)     # random number --> randn()

img = cv2.add(img, noise, dtype=cv2.CV_8UC3)

# SQ DIFF <-- Squared Difference
# Normed <-- Normalized
result = cv2.matchTemplate(img, tmp, cv2.TM_CCOEFF_NORMED)

b_fig = cv2.normalize(result, None,
                      0, 255,   # 최솟값, 최댓값
                      cv2.NORM_MINMAX,  # 정규화 기법 선택
                      cv2.CV_8U)    # 그림의 data type

# Location: 위치
minv, maxv, minLoc, maxLoc = cv2.minMaxLoc(result)

# th <-- template height
# tw <-- template width
(th, tw) = tmp.shape[:2]

# print(tmp.shape)
# print(th)
# print(tw)

cv2.rectangle(img, maxLoc,  # 점 a
              (maxLoc[0] + tw, maxLoc[1] + th),  # 점 b
              (0, 0, 255), 5)
# (0, 0, 255) (B, G, R) <-- 빨간색
# 2 <-- 직사각형을 그릴 때 선의 두께

cv2.imshow('img', img)
cv2.imshow('template', tmp)
cv2.imshow('normalize', b_fig)
cv2.waitKey()
cv2.destroyAllWindows()
