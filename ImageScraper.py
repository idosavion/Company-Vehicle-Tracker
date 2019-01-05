import cv2 as cv


class ImageScraper:

    def __init__(self, image_path):
        self.image_path = image_path

    def show_image(self, image, size=(740, 410)):
        image = cv.resize(image, size)
        cv.imshow(self.image_path, image)
        cv.waitKey(0)


def divide_image_to_tiles(im, tile):
    tiles = []
    w, h = im.shape[0] // tile, im.shape[1] // tile
    for row in range(tile):
        for col in range(tile):
            curr_tile = im[w * col:w * (col + 1), h * row:h * (row + 1), :]
            tiles.append(curr_tile)
    return tiles


