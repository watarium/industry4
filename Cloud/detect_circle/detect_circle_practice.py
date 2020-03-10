# import the necessary packages
import numpy as np
import argparse
import cv2
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

# load the image, clone it for output, and then convert it to grayscale
image = cv2.imread(args["image"])
output = image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# detect circles in the image
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, dp=2, minDist=1000, param1=50, param2=100)
# ensure at least some circles were found
if circles is not None:
	# convert the (x, y) coordinates and radius of the circles to integers
	circles = np.round(circles[0, :]).astype("int")
	# loop over the (x, y) coordinates and radius of the circles
	for (x, y, r) in circles:
		# draw the circle in the output image, then draw a rectangle
		# corresponding to the center of the circle
		cv2.circle(output, (x, y), r, (0, 255, 0), 4)
		cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)

	# Extract the circle
	# img[top : bottom, left : right]
	x = circles[0][0]
	y = circles[0][1]
	r = circles[0][2]
	extracted_image = image[y-r:y+r, x-r:x+r]
	# show the output image
	# cv2.imshow("output", np.hstack([image, output]))
	cv2.imshow("output", extracted_image)
	cv2.imwrite('sample.jpg', extracted_image)
	# cv2.waitKey(0)
	# cv2.destroyAllWindows()

else:
	print('A circle is not detected.')