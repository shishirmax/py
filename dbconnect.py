import pypyodbc
connection = pypyodbc.connect('Driver={SQL Server};Server=SHISHIRS;Database=shishir;uid=sa;pwd=sysadmin')
print("Connected")

connection.close()