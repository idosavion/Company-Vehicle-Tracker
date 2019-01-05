import csv


def write_log(attribs):
    header = ["Driver", "License plate", "Odometer", "Location"]
    with open("vehicle_log.csv", "w") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(header)
        for odometer_read in attribs.get("Odometer"):
            row = [attribs.get("Driver"), attribs["License number"], odometer_read, attribs["Location"]]
            csv_writer.writerow(row)
