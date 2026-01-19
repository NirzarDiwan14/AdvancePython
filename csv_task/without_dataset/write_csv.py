from data_class import Data
import csv

print("entered write csv file")
data_obj = Data(10000)
data = data_obj.get_data()

file_name = "users_raw.csv"

print("opening csv file to write...")
with open(file_name,"w") as csvfile:
    writer = csv.writer(csvfile)
    for row in data: 
        writer.writerow(row)

print("file write completed.")

