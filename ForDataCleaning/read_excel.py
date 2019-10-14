import pandas
df = pandas.read_excel("test.xlsx")
for index,row in df.iterrows():
    print(row[0])