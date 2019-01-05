
import cv2
import pyzbar.pyzbar as pyzbar

import ImageScraper


def decode(image_path):
    # Find barcodes and QR codes
    im = cv2.imread(image_path)
    for tile in [1, 2, 3, 5, 7]:
        tiles = ImageScraper.divide_image_to_tiles(im, tile)
        decoded_objects_list = [pyzbar.decode(t) for t in tiles]
        for decodedObjects in decoded_objects_list:
            for obj in decodedObjects:
                if obj.type == 'QRCODE':
                    print('Type : ', obj.type)
                    print('Data : ', obj.data, '\n')
                    return obj.data

#
# qrs = decode('images/Img_2.jpg')
# qrs2 = decode('images/Img_1.jpg')
# qrs3 = decode('images/Img_3.jpg')
