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
			file.write('----------------------------------------------------------------------\n')
			file.write("Original Address: \n")
			file.write(complete_address)
			file.write("\n")
			#this gives the formatted address
			file.write("Formatted Address: \n")
			file.write(parsed_json['results'][0]['formatted_address'])
			file.write("\n")
			#this gives the latitude
			file.write("Latitude: \n")
			file.write(str(parsed_json['results'][0]['geometry']['location']['lat']))
			file.write("\n")
			#this gives the longitude
			file.write("Longitude: \n")
			file.write(str(parsed_json['results'][0]['geometry']['location']['lng']))            
			file.write("\n")
			file.write('----------------------------------------------------------------------\n')
	elif len(parsed_json['results'])>1:
			file.write('----------------------------------------------------------------------')
			file.write("Original Address: ")
			file.write(complete_address)
			#this gives the formatted address
			file.write("Result 1:")
			file.write("Formatted Address 1: ")
			file.write(parsed_json['results'][0]['formatted_address'])            
			file.write("Latitude: ")
			file.write(parsed_json['results'][0]['geometry']['location']['lat'])            
			file.write("Longitude: ")
			file.write(parsed_json['results'][0]['geometry']['location']['lng'])
			file.write("Result 2:")
			file.write("Formatted Address 1: ")
			file.write(parsed_json['results'][0]['formatted_address'])            
			file.write("Latitude: ")
			file.write(parsed_json['results'][0]['geometry']['location']['lat'])            
			file.write("Longitude: ")
			file.write(parsed_json['results'][0]['geometry']['location']['lng'])            
			file.write('----------------------------------------------------------------------')
	else:
			file.write("No record available for: ")
			file.write(complete_address)
	return;
getResponse("County Road 141,Saint Augusta,MN,55320")
file.close() 