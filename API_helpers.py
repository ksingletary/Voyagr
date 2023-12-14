import requests
from dotenv import load_dotenv
import os
import random

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


def get_tokyo_pics():
    """API calls for Pics on pics page"""
    headers = {
    'accept': 'application/vnd.amadeus+json',
    'Authorization': f'Bearer {token}',
    }

    params = {
        'latitude': '35.710518',
        'longitude': '139.797733',
        'radius': '10'
    }

    response = requests.get(f'{API_BASE_URL}/shopping/activities', params=params, headers=headers)
    data = response.json()
    numb_rand = random.randrange(1,5)
    pics = []
    for pic in data['data'][numb_rand]['pictures']:
        pics.append(pic)
        if len(pics) == 12:
            break
    return pics

def get_rome_pics():
    """API calls for Pics on pics page"""
    headers = {
    'accept': 'application/vnd.amadeus+json',
    'Authorization': f'Bearer {token}',
    }

    params = {
        'latitude': '41.9028',
        'longitude': '12.4964',
        'radius': '20'
    }

    response = requests.get(f'{API_BASE_URL}/shopping/activities', params=params, headers=headers)
    data = response.json()
    numb_rand = random.randrange(1,10)
    pics = []
    for pic in data['data'][numb_rand]['pictures']:
        pics.append(pic)
        if len(pics) == 12:
            break
    return pics

def get_paris_pics():
    """API calls for Pics on pics page"""
    headers = {
    'accept': 'application/vnd.amadeus+json',
    'Authorization': f'Bearer {token}',
    }

    params = {
        'latitude': '48.8566',
        'longitude': '2.3522',
        'radius': '10'
    }

    response = requests.get(f'{API_BASE_URL}/shopping/activities', params=params, headers=headers)
    data = response.json()
    numb_rand = random.randrange(1,10)
    pics = []
    for pic in data['data'][numb_rand]['pictures']:
        pics.append(pic)
        if len(pics) == 12:
            break
    return pics

def get_dubai_pics():
    """API calls for Pics on pics page"""
    headers = {
    'accept': 'application/vnd.amadeus+json',
    'Authorization': f'Bearer {token}',
    }

    params = {
        'latitude': '25.2048',
        'longitude': '55.2708',
        'radius': '20'
    }

    response = requests.get(f'{API_BASE_URL}/shopping/activities', params=params, headers=headers)
    data = response.json()
    numb_rand = random.randrange(0,4)
    pics = []
    for pic in data['data'][numb_rand]['pictures']:
        pics.append(pic)
        if len(pics) == 12:
            break
    return pics

def get_egypt_pics():
    """API calls for Pics on pics page"""
    headers = {
    'accept': 'application/vnd.amadeus+json',
    'Authorization': f'Bearer {token}',
    }

    params = {
        'latitude': '29.9792',
        'longitude': '31.1342',
        'radius': '20'
    }

    response = requests.get(f'{API_BASE_URL}/shopping/activities', params=params, headers=headers)
    data = response.json()
    numb_rand = random.randrange(1,7)
    pics = []
    for pic in data['data'][numb_rand]['pictures']:
        pics.append(pic)
        if len(pics) == 12:
            break
    return pics


 
