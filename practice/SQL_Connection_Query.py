import pyodbc
import pandas as pd
connection = pyodbc.connect('Driver={SQL Server};Server=SHISHIRS;Database=AdventureWorks;uid=sa;pwd=sysadmin')
#data = pd.read_sql('SELECT COUNT(1) TotalRecords, CAST(SessionnStart As DATE) As Dates from homeSpotter.DimSession group by CAST(SessionnStart AS DATE) order by CAST(SessionnStart AS DATE) DESC')
#data.to_excel("DailyDataCount.xlsx",sheet_name='Records_Day')
data = pd.read_sql('SELECT AddressID,AddressLine1,AddressLine2,City FROM Person.Address',connection)
#data.to_excel('address.xlsx',encoding='sys.getfilesystemencoding()')
data.to_excel("address.xlsx",sheet_name='Sheet_name_1')
