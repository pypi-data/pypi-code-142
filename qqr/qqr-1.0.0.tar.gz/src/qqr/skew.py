# flake8: noqa

import math
import numpy as np
import cv2


class Skew:
    """Class to detect skew in an image."""

    def skew_XY(self, angle, x, y):
        '''
        Skew given coordinates by a provided angle using the tangent rule 

        Args: 
            angle: image that contains QR code
            x: X coordinate
            y: Y coordinate
        Returns:
            new_x: skewed X coodrinate
            new_y: skewed Y coordinate
        '''
        radian = np.deg2rad(angle)
        tangent = 1 / math.tan(radian)
        new_x = x
        new_y = round(y + (x * tangent))
        return new_x, new_y

    def shear(self, image, angle, newimage):
        '''
        Shear the new image based on the old one

        Args: 
            image: image that contains QR code
            angle: the angle of skew
            newimage: new image that contains QR code

        Returns:
            newimage: the sheared image of QR code
        '''
        x_mid, y_mid = image.shape[0]/2, image.shape[1]/2
        newimage_x_mid, newimage_y_mid = newimage.shape[0] / \
            2, newimage.shape[1]/2

        for row in range(0, image.shape[0]):
            for col in range(0, image.shape[1]):
                y_prime = y_mid - col
                x_prime = x_mid - row
                x_new, y_new = self.skew_XY(angle, x_prime, y_prime)

                xdist = int(newimage_x_mid - x_new)
                ydist = int(newimage_y_mid - y_new)
                if xdist < newimage.shape[0] and ydist < newimage.shape[1]:
                    newimage[xdist, ydist, :] = image[row, col, :]

        return newimage

    def canvasSize(self, image, degree):
        '''
        Generates image with a new size to hold the skewed QR

        Args: 
            img: image that contains QR code
            degree: the the degree of skew

        Returns:
            skewed_image_canvas: image that holds a skewed QR 
        '''

        row, col, num_channels = image.shape
        radian = np.deg2rad(degree)
        new_y_value = round(row + (col * (1 / math.tan(radian))))
        skewed_image_canvas = np.zeros((row, new_y_value, 3))
        return skewed_image_canvas

    def deskew(self, img):
        '''
        Warp the perspective of a given QR code to make a square

        Args: 
            img: image that contains QR code

        Returns:
            out: image of a deskewed QR code
        '''

        if len(img.shape) > 2:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        qr = cv2.QRCodeDetector()

        ret_qr, points = qr.detect(img)
        img_copy = np.copy(img)
        img_copy = cv2.cvtColor(img_copy, cv2.COLOR_BGR2RGB)
        if points is None:
            return img
        # Here, I have used L2 norm. You can use L1 also.
        width_AD = np.sqrt(((points[0][0][0] - points[0][1][0])
                           ** 2) + ((points[0][0][1] - points[0][1][1]) ** 2))
        width_BC = np.sqrt(((points[0][3][0] - points[0][2][0])
                           ** 2) + ((points[0][3][1] - points[0][2][1]) ** 2))
        maxWidth = max(int(width_AD), int(width_BC))

        height_AB = np.sqrt(
            ((points[0][0][0] - points[0][3][0]) ** 2) + ((points[0][0][1] - points[0][3][1]) ** 2))
        height_CD = np.sqrt(
            ((points[0][2][0] - points[0][1][0]) ** 2) + ((points[0][2][1] - points[0][1][1]) ** 2))
        maxHeight = max(int(height_AB), int(height_CD))

        input_pts = np.float32(
            [points[0][0], points[0][3], points[0][2], points[0][1]])
        output_pts = np.float32([[0, 0],
                                [0, maxHeight - 1],
                                [maxWidth - 1, maxHeight - 1],
                                [maxWidth - 1, 0]])

        # Compute the perspective transform M
        M = cv2.getPerspectiveTransform(input_pts, output_pts)

        out = cv2.warpPerspective(
            img, M, (maxWidth, maxHeight), flags=cv2.INTER_LINEAR)
        out = np.pad(array=out, pad_width=50,
                     mode='constant', constant_values=255)
        return out
