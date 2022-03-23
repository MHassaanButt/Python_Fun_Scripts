import cv2

#specify the path of input image
image1= cv2.imread('input_img.png')
window_name='Input Image'
#Displaying the input image
cv2.imshow(window_name, image1)

# converting image from one color space to another
grey_img= cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
invert = cv2.bitwise_not(grey_img)

#image smoothing
blur = cv2.GaussianBlur(invert, (21,21), 0)
invertedblur = cv2.bitwise_not(blur)
sketch = cv2.divide(grey_img, invertedblur, scale=256.0)

#save converted image
cv2.imwrite('output_img.png', sketch)

#read converted image
image= cv2.imread('output_img.png')
window_name='Output Image'
#Displaying the Sketch image

cv2.imshow(window_name, image)

#wait for user to press any key
cv2.waitKey(0)

#close all windows
cv2.destroyAllWindows()