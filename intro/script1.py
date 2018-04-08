import cv2

img = cv2.imread("galaxy.jpg", 0) # 0 for black/white 1 for color

print(type(img))
print(img) # matrix of img
print(img.shape)  # a tuple of number of rows, columns and channels
print(img.ndim) # check the dimension of array

resized_image = cv2.resize(img, (int(img.shape[1]/2),int(img.shape[0]/2)))
cv2.imshow("Galaxy", resized_image)
cv2.imwrite("Galaxy_resized.jpg", resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
