import pypyodbc
connection = pypyodbc.connect('Driver={SQL Server};Server=SHISHIRS;Database=shishir;uid=sa;pwd=sysadmin')
print("Connected....")
cursor = connection.cursor() 
SQLCommand = ("SELECT * INTO tmpTblEmp FROM tblEmployee")
cursor.execute(SQLCommand)
print("Query Executed...")
connection.commit()
connection.close()