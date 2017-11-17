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
    else:
            print("No record available for: ",complete_address)
    return;

getResponse("Lot 2 140th Ave,Beaver Twp,WI,54889")
getResponse("Gitasri Clinic, Dhanbad, Jharkhand")
#getResponse("Contata Solutions Noida India")
#getResponse("IIT(ISM) Dhanbad, Jharkhand, India")