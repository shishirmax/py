import csv
import pandas
df = pandas.read_excel("test.xlsx")
with open('test.csv', 'w') as csvfile:
    spamwriter = csv.writer(csvfile,delimiter = '|',lineterminator='\n')
    for index,row in df.iterrows():
        spamwriter.writerow([row[0],row[1],row[2]])
    
