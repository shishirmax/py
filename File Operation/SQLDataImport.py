import pypyodbc
#db connection str
connection = pypyodbc.connect('Driver={SQL Server};Server=SHISHIRS;Database=shishir;uid=sa;pwd=sysadmin')
print("Connected....")
#fetching input data
print("Enter Name")
name = input()
cursor = connection.cursor()
SQLCommand = ("INSERT INTO pyTestDB(name) VALUES(?)")
Values = [name]
#Query Processing
cursor.execute(SQLCommand,Values)
#Commiting any pending transaction to the database.
connection.commit()
#closing connection
print("Data Successfully Inserted")
connection.close()