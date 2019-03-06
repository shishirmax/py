import pyodbc
import pandas as pd
connection = pyodbc.connect('Driver={SQL Server};Server=SHISHIRS;Database=AdventureWorks;uid=sa;pwd=sysadmin')
data = pd.read_sql('SELECT AddressID,AddressLine1,AddressLine2,City FROM Person.Address',connection)
#data.to_excel('address.xlsx',encoding='sys.getfilesystemencoding()')
data.to_excel("address.xlsx",sheet_name='Sheet_name_1')
