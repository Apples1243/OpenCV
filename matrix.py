import cv2

img = cv2.imread('cat.bmp', cv2.IMREAD_COLOR)   # cv2.IMREAD_GRAYSCALE로 하면 회색으로 나옴

# ndarray <--- n-dimensional array (n-차원의 배열)
print(type(img))    # img 변수에 저장된 데이터의 타입(자료형) <class 'numpy.ndarray'>
print(img.shape)    # img 변수가 어떤 구조인지 확인 (480, 640)

cv2.namedWindow('image')
cv2.imshow('image', img)
cv2.waitKey()
cv2.destroyAllWindows()
