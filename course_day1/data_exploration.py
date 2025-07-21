import csv


def get_data(filename):
    with open(filename, "r") as input_file:
        data = csv.DictReader(input_file)
        return [record for record in data]
