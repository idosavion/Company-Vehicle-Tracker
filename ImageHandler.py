import GeoDataExtracter
import ImageOdometerScraper
import ImageQRScraper


def extract_attributes(image_path):
    image_data = {
        "Odometer": ImageOdometerScraper.find_odometer_text(image_path),
        "License number": ImageQRScraper.decode(image_path),
        "Location": GeoDataExtracter.get_exif_location(image_path)}
    return image_data