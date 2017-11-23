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

#getResponse("1021 Bailey Street, Hastings, 55033")

#getResponse("805 Flying Cloud Dr #219   Eden Prairie, MN, 55344")
#getResponse("503 11th Ave NE Minot, ND, 58703")
#getResponse("3711 Pillsbury Ave S Minneapolis, MN, 55409")
#c/o 12502 Chaney Avenue	NA	Lismore	MN	56155
getResponse("contata solutions india")
#getResponse("15104 Southwind Drive , Burnsville,, 55306")
#getResponse("3305 148th Street West , Rosemount, 55068")
#getResponse("14550 240th Street East, Hastings, 55033")
#getResponse("4107 Cashell Glen, Eagan, 55122")
#getResponse("Lot 2 140th Ave,Beaver Twp,WI,54889")
#getResponse("XXX Jackson Avenue N,Morristown,MN,55052")
#getResponse("Lot 27 Birch Park,St. Joseph Twp,WI,54016")
#getResponse("AAAA Cedar Lake Boulevard,Faribault,MN,55021")
#getResponse("Contata Solutions Noida India")
#getResponse("IIT(ISM) Dhanbad, Jharkhand, India")