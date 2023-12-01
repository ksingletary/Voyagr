import requests
# from secret import KEY, API_SECRET
from dotenv import load_dotenv
import os

API_BASE_URL = "https://test.api.amadeus.com/v1"

def configure():
    load_dotenv()

configure()

def new_token():
    """Generate new token after each request. Exp: 30 minutes"""

    data = {
    'grant_type': 'client_credentials',
    'client_id': os.getenv('KEY'),
    'client_secret': os.getenv('API_SECRET')
    }

    response = requests.post('https://test.api.amadeus.com/v1/security/oauth2/token', data=data)
    data = response.json()
    new_token = data['access_token']
    return new_token
    
token = new_token()


def get_pics():
    """API calls for Pics on home page"""
    headers = {
    'accept': 'application/vnd.amadeus+json',
    'Authorization': f'Bearer {token}',
    }

    params = {
        'latitude': '35.710518',
        'longitude': '139.797733'
    }

    response = requests.get(f'{API_BASE_URL}/shopping/activities/3269072', params=params, headers=headers)
    data = response.json()
    pictures = data['data']['pictures']
    req_pic_ident = '4iog'              #api randomizes pictures list, so we use pic link identifier to get correct pic

    my_pic1 = ''

    for pic in pictures:
        if req_pic_ident in pic:
            my_pic1 = pic

    response2 = requests.get(f'{API_BASE_URL}/shopping/activities/6379055', headers=headers)
    data2 = response2.json()
    pictures_list_2 = data2['data']['pictures']
    req_pic_ident2 = '1453892'   

    my_pic2 = ''

    for pic2 in pictures_list_2:
        if req_pic_ident2 in pic2:
            my_pic2 = pic2  

    response3 = requests.get(f'{API_BASE_URL}/shopping/activities/3273216', headers=headers)
    data3 = response3.json()
    pictures_list_3 = data3['data']['pictures']
    req_pic_ident3 = 'n8ij'   

    my_pic3 = ''

    for pic3 in pictures_list_3:
        if req_pic_ident3 in pic3:
            my_pic3 = pic3 


    return my_pic1, my_pic2, my_pic3


    # res = requests.get("https://test.api.amadeus.com/v1/shopping/activities",
    #                        params={'latitude': 41.390205, 'longitude': 2.154007, 'radius': 1},
    #                        headers={'Authorization': f'Bearer {token}', 'accept': 'application/vnd.amadeus+json'}
                        #    )
