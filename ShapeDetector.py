import os
import cv2 as cv
from pytesseract import image_to_string


def poligon_extracter(img_for_box_extraction_path,destanation_folder):
    if not os.path.exists(destanation_folder):
        os.mkdir(destanation_folder)
    img = cv.imread(img_for_box_extraction_path, 1)

    red_channel = img[:, :, 2]

    ret, thresh = cv.threshold(red_channel, 80, 255, 1)
    im, contours, h = cv.findContours(thresh, 1, 2)
    for i, cnt in enumerate(contours):
        approx = cv.approxPolyDP(cnt, 0.01 * cv.arcLength(cnt, True), True)
        if len(approx) == 5:
            # cv.drawContours(img, [cnt], 0, 255, -1)
            pass
        elif len(approx) == 3:
            pass
            # cv.drawContours(img, [cnt], 0, (0, 255, 0), -1)
        elif len(approx) == 4:

            # cv.drawContours(img, [cnt], 0, (0, 0, 255), -1)
            x, y, w, h = cv.boundingRect(cnt)
            if w < 80 or h < 20:
                continue
            cropped = img[y:y + h, x:x + w]
            cv.imwrite(os.path.join(destanation_folder,str(i) + '.jpg'), cropped)


poligon_extracter('images/Img_2.jpg','im2_crops')
poligon_extracter('images/Img_1.jpg','im1_crops')

# poligon_extracter('th1.jpg')

print('im2 crops')
for file in os.listdir('im2_crops'):
    path = os.path.join('im2_crops', file)
    print(image_to_string(path))

print('im1 crops')
for file in os.listdir('im1_crops'):
    path = os.path.join('im1_crops', file)
    print(image_to_string(path))


