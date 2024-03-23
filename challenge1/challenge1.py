import cv2
import numpy as np



img = cv2.imread("AIQ - Management Trainee Assignment - Challenge_1 (1).jpg")
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)


range1 = (23,0,0)
range2 = (255,255,255)
mask = cv2.inRange(hsv,range1,range2)


kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7,7))
mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

mask = cv2.merge([mask,mask,mask])

mask_inv = 255 - mask

white = np.full_like(img, (255,255,255))

img_masked = cv2.bitwise_and(img, mask)

white_masked = cv2.bitwise_and(white, mask_inv)

result = cv2.add(img_masked, mask_inv)

cv2.imwrite("coin_mask.png", mask)
cv2.imwrite("coin_white_background.jpg", result)
