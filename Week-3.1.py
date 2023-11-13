
# importing the modules needed
import cv2
import numpy as np
# Reading the image
image = cv2.imread('mando.jpg')
# Creating the kernel (2d convolution matrix) 
kernel1 = np.ones((5, 5), np.float32)/30
# Applying the filter2D() function
print(kernel1)
img = cv2.filter2D(src=image, ddepth=-1, kernel=kernel1)
# Shoeing the original and output image
cv2.imshow('Original', image)
cv2.imshow('Kernel Blur', img)
cv2.waitKey()
cv2.destroyAllWindows()