import pyodbc
connection = pyodbc.connect('Driver={SQL Server};Server=SHISHIRS;Database=shishir;uid=sa;pwd=sysadmin')
print("Connected...")
cursor = connection.cursor()
cursor.execute("SELECT Employee_id,First_name,Last_name,Salary,Department,Joining_date FROM Employee")
for row in cursor.fetchall():
    print(row)