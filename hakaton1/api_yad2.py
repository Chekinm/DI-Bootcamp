from requests import get
import json


async def get_yad2_data(request_params) -> dict:
    """make an api request to yad2 using request_params dict
    get back a dictionary with desired flats 
    we need a link a number of room and photos urls list for a POC prototype
    """
    
    # some parameters a still hardcoded, need testing which on eshould be tuned by users
 
    payload = { 
            'cat' : "2",
            'subcat' : "2",
            'price' : "1000-27000", # will add price selection in next release
            'airConditioner' : "1",  # don't think anybody need flat whitout:)
            'balcony' : f"{int(request_params[5])}",
            'longTerm' : "1",     # 
            'squaremeter' : f"{request_params[6]}-{request_params[7]}",
            'z' : "14",   # don't know what it means
            'center_point[]' : f"{request_params[3]},{request_params[2]}",
            'distance[]' : f"{request_params[4]}",
            'isMapView': '1',
            'page' : '1'    
        }

    print(payload)
    try:
        
        yad2_response = get('https://www.yad2.co.il/api/feed/get', params=payload)

        if yad2_response.status_code == 200:
            print('yad2 is good today')

            yad2_response_dict = json.loads(yad2_response.content)
            
        else:
            print('We exireinced a porblem with scraping. Get you a Rishon json instead.')
            with open('json_data.json', 'r') as outfile:
                yad2_response_dict = json.load(outfile)
    except json.JSONDecodeError as e:
        print ('Looks like yad 2 banned us again change IP. Get you a defult Rishon json instead.')
        with open('json_data.json', 'r') as outfile:
            yad2_response_dict = json.load(outfile)
    
    return  yad2_response_dict
