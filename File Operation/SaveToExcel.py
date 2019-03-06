import pyodbc
import pandas as pd 
connection = pyodbc.connect('Driver={SQL Server};Server=SHISHIRS;Database=shishir;uid=sa;pwd=sysadmin')
data = pd.read_sql('SELECT * FROM Employee',connection)
data.to_excel('EmployeeData.xls')