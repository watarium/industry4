# import the necessary packages
import numpy as np
import argparse, os, random
import cv2

class Detect_circle:
    def save_file(self, filename):
        # load the image, clone it for output, and then convert it to grayscale
        if os.path.exists(filename):
            image = cv2.imread(filename)
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
                extracted_image = image[y - r:y + r, x - r:x + r]
                # show the output image
                # cv2.imshow("output", np.hstack([image, output]))
                # cv2.imshow("output", extracted_image)
                output_filename = filename.strip('/original_sample''.jpg') + '_circle.jpg'
                print(output_filename)
                cv2.imwrite(output_filename, extracted_image)
                # cv2.waitKey(0)
                # cv2.destroyAllWindows()

            else:
                print('A circle is not detected.')

    def save_rotate_file(self, filename):
        # load the image, clone it for output, and then convert it to grayscale
        if os.path.exists(filename):
            image = cv2.imread(filename)

            # rotation
            height = image.shape[0]
            width = image.shape[1]
            center = (int(width / 2), int(height / 2))
            # random rotate
            angle = random.randint(1, 360)
            scale = 1.0
            trans = cv2.getRotationMatrix2D(center, angle, scale)
            image = cv2.warpAffine(image, trans, (width, height))

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
                # cv2.imshow("output", extracted_image)
                output_filename = filename.strip('/original_sample''.jpg') + '_circle.jpg'
                print(output_filename)
                cv2.imwrite(output_filename, extracted_image)
                # cv2.waitKey(0)
                # cv2.destroyAllWindows()

            else:
                print('A circle is not detected.')