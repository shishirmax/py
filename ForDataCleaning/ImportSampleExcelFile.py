import pyodbc
import pandas
df = pandas.read_excel("SampleData.xlsx")
connection = pyodbc.connect('Driver={SQL Server};Server=localhost\SQLEXPRESS;Database=Analytics;uid=;pwd=;Integrated Security=True')
cursor = connection.cursor()

for index,row in df.iterrows():
    cursor.execute("INSERT INTO Question([Question]) values (?)",row[0])
    connection.commit()
cursor.close()
connection.close()