import csv
input_file = open("HS.csv","r+")
reader_file = csv.reader(input_file)
value = len(list(reader_file))
print(value) 