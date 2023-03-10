import cv2

src = cv2.imread('rose.bmp', cv2.IMREAD_GRAYSCALE)

for ksize in (3, 5, 7):
    dst = cv2.blur(src, (ksize, ksize))

    txt = "Mean: (%d x %d)" % (ksize, ksize)

    cv2.putText(dst, txt, (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                1.0, 255, 3, cv2.LINE_AA)
    # 1.0 : 폰트 스케일
    # 255 : 폰트 색
    # 1   : 선 타입
    cv2.imshow('Result', dst)
    cv2.waitKey()
cv2.destroyAllWindows()
