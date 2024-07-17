import csv


def read_csv(filename):
    with open(filename, "r") as datafile:
        reader = csv.DictReader(datafile)
        result = []
        for row in reader:
            result.append(
                {
                    "ID": int(row["#"]),
                    "Name": row["Name"],
                    "Type 1": row["Type 1"],
                    "Type 2": row["Type 2"],
                    "Total": int(row["Total"]),
                    "HP": int(row["HP"]),
                    "Attack": int(row["Attack"]),
                    "Defense": int(row["Defense"]),
                    "Special Attack": int(row["Sp. Atk"]),
                    "Special Defense": int(row["Sp. Def"]),
                    "Speed": int(row["Speed"]),
                    "Generation": int(row["Generation"]),
                    "Legendary": True if row["Legendary"] == "True" else False,
                }
            )
        return result
