import cv2 as cv

img = cv.imread('/Users/sofyamalashchenko/Desktop/Screen Shot 2022-01-31 at 3.22.58 PM.png')
#Takes in a path to an image and returns it as a matric of pixels


cv.imshow("Test", img)
# Displays the image as a new window
# The first parameter is the name of the window
# The second one is the matrix of pixels

