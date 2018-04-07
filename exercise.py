import cv2

kangaroos = cv2.imread("kangaroos-rain-australia_71370_990x742.jpg", 0)
lighthouse = cv2.imread("Lighthouse.jpg", 0)
moon = cv2.imread("Moon sinking, sun rising.jpg", 0)

kangaroo_resize = cv2.resize(kangaroos,(100,100))
lighthouse_resize = cv2.resize(lighthouse, (100,100))
moon_resize = cv2.resize(moon, (100,100))

cv2.imwrite("kangaroo_resized.jpg", kangaroo_resize)
cv2.imwrite("lighthouse_resized.jpg", lighthouse_resize)
cv2.imwrite("moon_resize.jpg", moon_resize)