import requests
import json
api_key = "AIzaSyBEQyAbIVXfGTSbLr_S-HUpSZoxfoBbc5I"
strAdd = "0 State Highway 99"
strCity = " Montgomery Twp"
strState = " "
strZip = "56069"
complete_address = strAdd+strCity+strState+strZip
url = "https://maps.googleapis.com/maps/api/geocode/json?address="+complete_address+"&key=AIzaSyBEQyAbIVXfGTSbLr_S-HUpSZoxfoBbc5I"
api_response = requests.get(url)
api_response.status_code
api_response.headers['content-type']
api_response.encoding
api_response.json()

json_r = api_response.json()
json_str = json.dumps(json_r)
parsed_json = json.loads(json_str)
print("Original Address: ",complete_address)
#this gives the formatted address
print("Formatted Address: ",parsed_json['results'][0]['formatted_address'])
#this gives the latitude
print("Latitude: ",parsed_json['results'][0]['geometry']['location']['lat'])
#this gives the longitude
print("Longitude: ",parsed_json['results'][0]['geometry']['location']['lng'])