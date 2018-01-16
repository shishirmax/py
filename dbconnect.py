import pypyodbc
connection = pypyodbc.connect('Driver={SQL Server};Server=SHISHIRS;Database=shishir;uid=sa;pwd=sysadmin')
#print("Connected")
cursor = connection.cursor()
SQLCommand = ("select * from product")
res = cursor.execute(SQLCommand)
for r in res:
	print(r)
connection.commit()
connection.close()