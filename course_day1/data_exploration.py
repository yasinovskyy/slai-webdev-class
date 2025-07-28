import csv


def read_data(filename):
    with open(filename, "r") as input_file:
        return [record for record in csv.DictReader(input_file)]
