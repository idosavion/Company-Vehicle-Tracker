from __future__ import print_function
import pyzbar.pyzbar as pyzbar
import numpy as np
import cv2

from ImageScraper import ImageScraper


class ImageQRScraper(ImageScraper):

    def decode(im):
        # Find barcodes and QR codes
        decodedObjects = pyzbar.decode(im)

        # Print results - only for debugging
        for obj in decodedObjects:
            print('Type : ', obj.type)
            print('Data : ', obj.data, '\n')

        return decodedObjects

    # Display barcode and QR code location
    def display(self, im, decodedObjects):
        # Loop over all decoded objects
        for decodedObject in decodedObjects:
            points = decodedObject.polygon

            # If the points do not form a quad, find convex hull
            if len(points) > 4:
                hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
                hull = list(map(tuple, np.squeeze(hull)))
            else:
                hull = points;

            # Number of points in the convex hull
            n = len(hull)

            # Draw the convext hull
            for j in range(0, n):
                cv2.line(im, hull[j], hull[(j + 1) % n], (255, 0, 0), 3)

        # Display results
        imS = cv2.resize(im, (960, 540))
        cv2.imshow(self.image_path,imS)
        cv2.waitKey(0)
