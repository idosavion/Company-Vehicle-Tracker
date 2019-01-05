import os
import re
import shutil

import cv2 as cv
from pytesseract import image_to_string

CROPPED_FOLDER = 'cropped'


def find_odometer_text(image_path):
    _extract_odometer_text(image_path, CROPPED_FOLDER)
    values = _determine_value(CROPPED_FOLDER)
    if len(values) == 0:
        print("No Text was found")
    return values



def _determine_value(folder_location):
    full_paths = [os.path.join(folder_location, f) for f in os.listdir(folder_location)]
    text_from_images = [image_to_string(p) for p in full_paths]
    only_digit_text = {re.sub('\D', '', t) for t in text_from_images}
    only_digit_text.remove('')
    shutil.rmtree(folder_location)
    return only_digit_text

def _extract_odometer_text(img_for_box_extraction_path, destanation_folder):
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
                continue
            cropped = img[y:y + h, x:x + w]
            cv.imwrite(os.path.join(destanation_folder, str(i) + '.jpg'), cropped)


print(find_odometer_text('images/Img_2.jpg'))
print(find_odometer_text('images/Img_1.jpg'))
# find_odometer_text('images/Img_1.jpg')
