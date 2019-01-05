import cv2 as cv


def show_image(self, image, size=(740, 410)):
    """
    here just for convenience and debugging
    """
    image = cv.resize(image, size)
    cv.imshow(self.image_path, image)
    cv.waitKey(0)


def divide_image_to_tiles(im, tile):
    """
    takes an image and divide it into tile ** 2 different tiles for recursive search
    """
    tiles = []
    w, h = im.shape[0] // tile, im.shape[1] // tile
    for row in range(tile):
        for col in range(tile):
            curr_tile = im[w * col:w * (col + 1), h * row:h * (row + 1), :]
            tiles.append(curr_tile)
    return tiles

