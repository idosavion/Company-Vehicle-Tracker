import exifread


# inspired by https://gist.github.com/snakeye/fdc372dbf11370fe29eb

def get_exif_location(image_path):
    """
    Returns the latitude and longitude, if available, from the provided exif_data (obtained through get_exif_data)
    """
    lat = 0
    lon = 0
    exif_data = _get_exif_data(image_path)
    gps_latitude = exif_data.get("GPS GPSLatitude")
    gps_latitude_ref = exif_data.get("GPS GPSLatitudeRef")
    gps_longitude = exif_data.get("GPS GPSLongitude")
    gps_longitude_ref = exif_data.get("GPS GPSLongitudeRef")

    gps_attributes_found = gps_latitude and gps_latitude_ref and gps_longitude and gps_longitude_ref
    if gps_attributes_found:
        lat = _convert_to_degress(gps_latitude)
        if gps_latitude_ref.values[0] != 'N':
            lat = 0 - lat

        lon = _convert_to_degress(gps_longitude)
        if gps_longitude_ref.values[0] != 'E':
            lon = 0 - lon
    return lat, lon


def _convert_to_degress(value):
    """
    Helper function to convert the GPS coordinates stored in the EXIF to degress in float format
    :param value:
    :type value: exifread.utils.Ratio
    :rtype: float
    """
    d = float(value.values[0].num) / float(value.values[0].den)
    m = float(value.values[1].num) / float(value.values[1].den)
    s = float(value.values[2].num) / float(value.values[2].den)

    return d + (m / 60.0) + (s / 3600.0)


def _get_exif_data(image_file):
    """
    extract the file's exif data
    :param image_file: image to extract
    :return: exif tags
    """
    with open(image_file, 'rb') as f:
        exif_tags = exifread.process_file(f)
    return exif_tags




