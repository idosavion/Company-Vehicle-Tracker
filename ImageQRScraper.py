from __future__ import print_function
import pyzbar.pyzbar as pyzbar
import numpy as np
import cv2

from ImageScraper import ImageScraper


class ImageQRScraper(ImageScraper):
    def decode(self):
        # Find barcodes and QR codes
        im = cv2.imread(self.image_path)
        decodedObjects = pyzbar.decode(im,scan_locations=True)

        # Print results
        for obj in decodedObjects:
            print('Type : ', obj.type)
            print('Data : ', obj.data, '\n')

        return decodedObjects


    # Display barcode and QR code location
    def display(im, decodedObjects):
        # Loop over all decoded objects
        for decodedObject in decodedObjects:
            points = decodedObject.polygon

            # If the points do not form a quad, find convex hull
            if len(points) > 4:
                hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
                hull = list(map(tuple, np.squeeze(hull)))
            else:
                hull = points

            # Number of points in the convex hull
            n = len(hull)

            # Draw the convext hull
            for j in range(0, n):
                cv2.line(im, hull[j], hull[(j + 1) % n], (255, 0, 0), 3)

        # Display results


jpg = 'images/Img_3.jpg'
qr_scraper = ImageQRScraper(jpg)
print(qr_scraper.decode())
