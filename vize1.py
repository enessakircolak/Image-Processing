import cv2
import numpy as np

#https://imageresizer.com/resize

img1 = cv2.imread("wiki.jpg")
img2 = cv2.imread("mando.jpg")

#cv2.imshow("resim1", img1)

toplam = cv2.addWeighted(img1,0.8,img2,0.2,0)

#cv2.imwrite("project.png",toplam)
cv2.imshow("resim", toplam)
cv2.waitKey(0)
cv2.destroyAllWindows()