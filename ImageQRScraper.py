
import cv2
import pyzbar.pyzbar as pyzbar

from ImageScraper import ImageScraper, divide_image_to_tiles


class ImageQRScraper(ImageScraper):
    def decode(self):
        # Find barcodes and QR codes
        im = cv2.imread(self.image_path)
        for tile in [1, 2, 3, 5, 7]:
            tiles = divide_image_to_tiles(im, tile)
            decoded_objects_list = [pyzbar.decode(t) for t in tiles]
            for decodedObjects in decoded_objects_list:
                for obj in decodedObjects:
                    if obj.type == 'QRCODE':
                        print('Type : ', obj.type)
                        print('Data : ', obj.data, '\n')
                        return obj.data


qrs = ImageQRScraper('images/Img_2.jpg')
qrs2 = ImageQRScraper('images/Img_1.jpg')
print(qrs.decode())
print(qrs2.decode())
