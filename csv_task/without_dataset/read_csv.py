import csv

file_name = "users_raw.csv"

print("Reading Started")
with open(file_name, "r") as csv_file:
    reader = csv.DictReader(csv_file)

    for line in reader:
        print(line)

print("Reading complete.")