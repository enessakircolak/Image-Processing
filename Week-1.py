import cv2
import numpy as np

resim1 = cv2.imread("mando.jpg")

cv2.imshow("mando.jpg",resim1)

print(resim1.size)

print(resim1.dtype)

print(resim1.shape)

cv2.waitKey(0)
cv2.destroyAllWindows()