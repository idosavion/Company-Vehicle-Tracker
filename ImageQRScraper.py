import cv2 as cv
import pyzbar.pyzbar as pyzbar
import ImageScraper


def decode(image_path):
    """
    look for qr code in the picture and divided into smaller tiles if not found
    :param image_path:
    :return:
    """
    im = cv.imread(image_path)
    for tile in [1, 2, 3, 5, 7]:  # prime number to avoid a case where the tile's edges will keep cutting the QR code
        tiles = ImageScraper.divide_image_to_tiles(im, tile)
        decoded_objects_list = [pyzbar.decode(t) for t in tiles]
        for decodedObjects in decoded_objects_list:
            for obj in decodedObjects:
                if obj.type == "QRCODE":
                    return obj.data.decode("ASCII")
    return "0"
