import os
import re
import shutil

import cv2 as cv
from pytesseract import image_to_string

CROPPED_FOLDER = "cropped"


def find_odometer_text(image_path):
    """
    Cropping the image into the rectangles found and searching for the odometer text in them
    :param image_path:
    :return: a set containing all the text suspected to be the odometer's
    """
    _extract_odometer_text(image_path, CROPPED_FOLDER)
    values = _determine_value(CROPPED_FOLDER)
    if len(values) == 0:
        print("No Text was found")
    if len(values) > 1:
        print("More then 1 image was found, multiply rows will be inserted to log file")
    return values


def _determine_value(folder_location):
    """

    :param folder_location: the location of the folder containing the cropped parts of the image
    :return: the text found in those pictures after filtering non numeric chars and text of unrealistic length for
    robustness
    """
    full_paths = [os.path.join(folder_location, f) for f in os.listdir(folder_location)]
    text_from_images = [image_to_string(p) for p in full_paths]
    only_digit_text = {re.sub('\D', '', t) for t in text_from_images}
    only_digit_text.remove('')
    only_digit_text = {t for t in only_digit_text if 4 < len(t) < 10}
    shutil.rmtree(folder_location)
    return only_digit_text


def _extract_odometer_text(img_for_box_extraction_path, destanation_folder):
    """
    Detects red contours in the picture, check if they are rectangles and they're shape satisfies the conditions,
    save them to the newly created folder :param img_for_box_extraction_path: image to search in :param
    destanation_folder: folder to save cropped parts into
    """
    if not os.path.exists(destanation_folder):
        os.mkdir(destanation_folder)
    img = cv.imread(img_for_box_extraction_path, 1)
    red_channel = img[:, :, 2]
    ret, thresh = cv.threshold(red_channel, 80, 255, 1)
    im, contours, h = cv.findContours(thresh, 1, 2)
    for i, cnt in enumerate(contours):
        approx = cv.approxPolyDP(cnt, 0.01 * cv.arcLength(cnt, True), True)
        if len(approx) == 4:
            x, y, w, h = cv.boundingRect(cnt)
            if w < 80 or h < 20:
                continue  # arbitrary limitation so small rectangles found won't be a problem
            cropped = img[y:y + h, x:x + w]
            cv.imwrite(os.path.join(destanation_folder, str(i) + '.jpg'), cropped)
