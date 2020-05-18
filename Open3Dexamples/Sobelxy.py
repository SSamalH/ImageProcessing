
import cv2
import numpy as np 
from matplotlib import pyplot as plt



# path 
path = r'C:\Users\ssamal\source\repos\ImageProcessing\Kolben_IO_01_01.tif'

# loading a grayscale image
img = cv2.imread(path, 0)

# Showing laplacian, sobelx and sobely filters

laplacian = cv2.Laplacian(img, cv2.CV_16SC1)
sobelx = cv2.Sobel(img,cv2.CV_16SC1,1,0, ksize=5)
# continue with y 
sobely = cv2.Sobel(img,cv2.CV_16SC1,0,1, ksize=5)

# Plotting graphs

plt.subplot(2,2,1), plt.imshow(img, cmap='gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2), plt.imshow(laplacian, cmap='gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3), plt.imshow(sobelx, cmap='gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,4), plt.imshow(sobely, cmap='gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
plt.show()

# Displaying a grayscale image
#cv2.imshow('Kolben', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
