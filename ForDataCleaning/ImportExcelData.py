import pyodbc
import pandas
df = pandas.read_excel("195841LeadCapture.xlsx")
connection = pyodbc.connect('Driver={SQL Server};Server=localhost\SQLEXPRESS;Database=Analytics;uid=;pwd=;Integrated Security=True')
cursor = connection.cursor()

for index,row in df.iterrows():
    cursor.execute("INSERT INTO LeadCapture([Date],[Name],[Company],[Title],[Phone],[Email],[Country],[RequestQuestion],[Page],[Country_2],[State_Region],[County_District],[City],[IP],[Device],[OS],[Browser]) values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17]))
    connection.commit()
cursor.close()
connection.close()