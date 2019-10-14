import csv
import pandas
df = pandas.read_excel("SampleData.xlsx")
with open('SampleData_1.csv', 'w') as csvfile:
    spamwriter = csv.writer(csvfile,delimiter = '|',lineterminator='\n')
    for index,row in df.iterrows():
        spamwriter.writerow([row[0]])
    
