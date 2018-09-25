import requests
import json
import pypyodbc

connection = pypyodbc.connect('Driver={SQL Server};Server=SHISHIRS;Database=shishir;uid=sa;pwd=sysadmin')
print("SQL Connection Created..")
print('----------------------------------------------------------------------')
def getToken(username,password):
    url = "https://api2.club-os.com/authenticate?username="+username+"&password="+password
    api_response = requests.get(url)
    api_response.status_code
    api_response.headers['content-type']
    api_response.encoding
    api_response.json()
    #print(api_response.json())
    json_r = api_response.json()
    json_str = json.dumps(json_r)
    parsed_json = json.loads(json_str)
    #print(parsed_json)
    
    #print('----------------------------------------------------------------------')
    #print(parsed_json['token'])
    strToken = parsed_json['token']
    cursor = connection.cursor()
    SQLCommand = ("INSERT INTO ApiToken(Token) VALUES(?)")
    Values = [strToken]
    cursor.execute(SQLCommand,Values)
    connection.commit()
    print("Data Successfully Inserted")
    connection.close()
    #print(strToken)
getToken("devs@anytimefitness.com","qoe2lGF4POeEX9j")


