import csv


def read_csv(filename):
    with open(filename, "r") as datafile:
        reader = csv.DictReader(datafile)
        return [item for item in reader]


def hello():
    print("hello")


hello()
read_csv("pokemon.csv")
