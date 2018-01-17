import requests
import json

file = open("Address.txt","w")
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
            file.write('----------------------------------------------------------------------')
            file.write("Original Address: ",complete_address)
            #this gives the formatted address
            file.write("Formatted Address: ",parsed_json['results'][0]['formatted_address'])
            #this gives the latitude
            file.write("Latitude: ",parsed_json['results'][0]['geometry']['location']['lat'])
            #this gives the longitude
            file.write("Longitude: ",parsed_json['results'][0]['geometry']['location']['lng'])            
            file.write('----------------------------------------------------------------------')
    elif len(parsed_json['results'])>1:
            file.write('----------------------------------------------------------------------')
            file.write("Original Address: ",complete_address)
            #this gives the formatted address
            file.write("Result 1:")
            file.write("Formatted Address 1: ",parsed_json['results'][0]['formatted_address'])            
            file.write("Latitude: ",parsed_json['results'][0]['geometry']['location']['lat'])            
            file.write("Longitude: ",parsed_json['results'][0]['geometry']['location']['lng'])
            file.write("Result 2:")
            file.write("Formatted Address 1: ",parsed_json['results'][0]['formatted_address'])            
            file.write("Latitude: ",parsed_json['results'][0]['geometry']['location']['lat'])            
            file.write("Longitude: ",parsed_json['results'][0]['geometry']['location']['lng'])            
            file.write('----------------------------------------------------------------------')
    else:
            file.write("No record available for: ",complete_address)	
    return;

 getResponse("100 Salem Church Road First door in circular drive. Sunfish Lake, MN, 55118")
 
 file.close() 
	