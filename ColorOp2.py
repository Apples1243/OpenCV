import cv2

src = cv2.imread('candies.png', cv2.IMREAD_COLOR)

# split : v. 쪼개다
bgr_p = cv2.split(src)


cv2.imshow('src', src)
cv2.imshow('Blue', bgr_p[0])
cv2.imshow('Green', bgr_p[1])
cv2.imshow('Red', bgr_p[2])

cv2.waitKey()
cv2.destroyAllWindows()
