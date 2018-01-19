import pypyodbc
import requests
import json

def getResponse(complete_address):    
    url = "https://maps.googleapis.com/maps/api/geocode/json?address="+complete_address+"&key=AIzaSyBEQyAbIVXfGTSbLr_S-HUpSZoxfoBbc5I"
    api_response = requests.get(url)
    api_response.status_code
    api_response.headers['content-type']
    api_response.encoding
    api_response.json()

    json_r = api_response.json()
    json_str = json.dumps(json_r)
    parsed_json = json.loads(json_str)
    #print(len(parsed_json['results']))
    if len(parsed_json['results'])>0:          
            print('----------------------------------------------------------------------')
            print("Original Address: ",complete_address)
            #this gives the formatted address
            print("Formatted Address: ",parsed_json['results'][0]['formatted_address'])
            #this gives the latitude
            print("Latitude: ",parsed_json['results'][0]['geometry']['location']['lat'])
            #this gives the longitude
            print("Longitude: ",parsed_json['results'][0]['geometry']['location']['lng'])            
            print('----------------------------------------------------------------------')
    elif len(parsed_json['results'])>1:
            print('----------------------------------------------------------------------')
            print("Original Address: ",complete_address)
            #this gives the formatted address
            print("Result 1:")
            print("Formatted Address 1: ",parsed_json['results'][0]['formatted_address'])            
            print("Latitude: ",parsed_json['results'][0]['geometry']['location']['lat'])            
            print("Longitude: ",parsed_json['results'][0]['geometry']['location']['lng'])
            print("Result 2:")
            print("Formatted Address 1: ",parsed_json['results'][0]['formatted_address'])            
            print("Latitude: ",parsed_json['results'][0]['geometry']['location']['lat'])            
            print("Longitude: ",parsed_json['results'][0]['geometry']['location']['lng'])            
            print('----------------------------------------------------------------------')
    else:
            print("No record available for: ",complete_address)
    return;

connection = pypyodbc.connect('Driver={ODBC Driver 13 for SQL Server};PORT=1443;Server=contata.database.windows.net;Database=Edina_QA;uid=contata.admin;pwd=C@ntata123')
#print("Connected")


cursor = connection.cursor()
#OriginalAddress = ("select top 10 OriginalAddress from zerorez.tblZerorezStandardAddressApi where formatted_address = 'NA' order by 1")
OriginalAddress = ("select case when OriginalAddress like ''%(%)%'' then substring(OriginalAddress,1,charindex(''('',OriginalAddress)-1)+''''+substring(OriginalAddress,charindex('')'',OriginalAddress)+1,len(OriginalAddress)) else originalAddress end updatedAddress from zerorez.tblZerorezStandardAddressApi(NOLOCK) where formatted_address = ''NA''  and originaladdress like ''%(%)%''")
res = cursor.execute(OriginalAddress)
for r in res:
	getResponse(str(r))
connection.commit()
connection.close()