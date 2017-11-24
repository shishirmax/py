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
#707 Commerce Drive, #410   Woodbury, MN, 55125
#getResponse("707 Commerce Drive, 410   Woodbury, MN, 55125")
#1125 1st Street South #229   Sartell, MN, 56377
#getResponse("1125 1st Street South 229   Sartell, MN, 56377")
#115 2nd Avenue South, #716   Minneapolis, MN, 55401
#getResponse("115 2nd Avenue South, 716   Minneapolis, MN, 55401")
#433 7th Street South, #1607   Minneapolis, MN, 55415
#getResponse("433 7th Street South, 1607   Minneapolis, MN, 55415")
#526 Lovell Ave #4   Roseville, MN, 55113
#getResponse("26 Lovell Ave 4   Roseville, MN, 55113")
#2996 Cleveland Ave N #109 Roseville, MN, 55113
#getResponse("2996 Cleveland Ave N 109 Roseville, MN, 55113")
#getResponse("2996 Cleveland Ave N #109 Roseville, MN, 55113")

#815 Smetana Rd #5 Hopkins,  , 55343
#getResponse("815 Smetana Rd #5 Hopkins,  , 55343")
#getResponse("815 Smetana Rd 5 Hopkins,  , 55343")

#526 Lovell Ave #4   Roseville, MN, 55113
#getResponse("526 Lovell Ave #4   Roseville, MN, 55113")
#getResponse("526 Lovell Ave 4   Roseville, MN, 55113")

#14221 Dallas Parkway #1000 *C1206s7***1704476084* Dallas, MN, 75254-2916 [excluding # also does not gives result]
#getResponse("14221 Dallas Parkway #1000 *C1206s7***1704476084* Dallas, MN, 75254-2916")
#getResponse("14221 Dallas Parkway 1000  Dallas, MN, 75254")

#707 Commerce Drive, #410   Woodbury, MN, 55125
#getResponse("707 Commerce Drive, #410   Woodbury, MN, 55125")
#getResponse("707 Commerce Drive, 410   Woodbury, MN, 55125")


#2670 Commerce Blvd #201 Mound, MN, 55364
#getResponse("2670 Commerce Blvd #201 Mound, MN, 55364")
#getResponse("2670 Commerce Blvd 201 Mound, MN, 55364")

#316 10th Ave SE   Minneapolis,  , 55414-1922
#getResponse("316 10th Ave SE   Minneapolis,  , 55414-1922")

#8770 West Bryn Mawr Ste #1300, Chicago IL, 60631
getResponse("8770 West Bryn Mawr Ste 1300, Chicago IL, 60631")
