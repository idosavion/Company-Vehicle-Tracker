import csv

import os

VEHICLE_LOG_CSV = "vehicle_log.csv"


def write_log(log_data_dict):
    """
    write the new rows to log file, append them at the end if file is already exist
    :param log_data_dict: dictionary with data to add
    :return:
    """
    header = ["Driver", "License plate", "Odometer", "Location"]
    rows = []
    for odometer_read in log_data_dict.get("Odometer"):
        rows.append(
            [log_data_dict.get("Driver"), log_data_dict["License number"], odometer_read, log_data_dict["Location"]])
    if os.path.exists(VEHICLE_LOG_CSV):
        with open(VEHICLE_LOG_CSV, "a") as csv_file:
            _add_rows_to_log(rows, csv_file)
    else:
        with open(VEHICLE_LOG_CSV, "w") as csv_file:
            _add_rows_to_log([header] + rows, csv_file)


def _add_rows_to_log(rows, open_file):
    """
    receive the file and write the rows into it
    :param rows: rows to write
    :param open_file: file to write into
    :return:
    """
    csv_writer = csv.writer(open_file)
    for row in rows:
        csv_writer.writerow(row)
