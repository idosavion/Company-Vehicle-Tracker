import GeoDataExtracter
import ImageOdometerScraper
import ImageQRScraper


def extract_attributes(image_path):
    image_data = {
        "Odometer": ImageOdometerScraper.find_odometer_text(image_path),
        "License number": ImageQRScraper.decode(image_path),
        "Location": GeoDataExtracter.get_exif_location(image_path)}
    if image_data.get("License number") is None:
        print("Could not detect QR sticker - writing 0 instead")
    if image_data.get("Location") is None:
        print("Could not detect location - writing (0,0) instead")
    if image_data.get("Odometer") is None:
        print("Could not detect odometer - writing 0 instead")
    return image_data


