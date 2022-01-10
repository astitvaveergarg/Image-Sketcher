import cv2

def imagesize(img):
    scale_percent = 10 # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
  
    image = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    return image

image = cv2.imread(input("Enter Full Path Of File: "))
image=imagesize(image)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
inverted_image = 250 - gray_image
blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)
inverted_blurred = 250- blurred
pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=250.0)
cv2.imshow("Original Image", image)
cv2.imwrite("Pencil Sketch of User Photo.jpeg", pencil_sketch)
cv2.waitKey(0)