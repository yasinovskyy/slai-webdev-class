import csv


def read_csv(filename):
    with open(filename, "r") as datafile:
        data = csv.DictReader(datafile)
        return [row for row in data]
