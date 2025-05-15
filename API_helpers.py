import requests
from dotenv import load_dotenv
import os
import random

"""The AMADEUS FOR DEVELOPERS API is still in beta. It is still somewhat buggy, but will show the
pictures if you re-generate batch, or navigate out and back into pics page. It's having a hard time with
Paris and Rome, but the other locations seem to work fine.
"""

API_BASE_URL = "https://test.api.amadeus.com/v1"
DEFAULT_MAX_PICS = 10

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

    try:
        response = requests.post('https://test.api.amadeus.com/v1/security/oauth2/token', data=data)
        response.raise_for_status()
        data = response.json()
        new_token = data['access_token']
        return new_token
    except requests.exceptions.RequestException as e:
        print(f"Error getting token: {e}")
        return None
    except KeyError:
        print("Error: Unable to extract access token from response")
        return None

try:
    token = new_token()
except Exception as e:
    print(f"Error initializing token: {e}")
    token = None

def get_location_pics(latitude, longitude, radius, max_index, max_pics=DEFAULT_MAX_PICS):
    """
    Generic function to get pictures for a location

    Args:
        latitude (str): Latitude coordinate
        longitude (str): Longitude coordinate
        radius (str): Search radius in km
        max_index (int): Maximum random index to use
        max_pics (int, optional): Maximum number of pictures to return. Defaults to DEFAULT_MAX_PICS.

    Returns:
        list: List of picture URLs
    """
    if not token:
        return []

    headers = {
        'accept': 'application/vnd.amadeus+json',
        'Authorization': f'Bearer {token}',
    }

    params = {
        'latitude': latitude,
        'longitude': longitude,
        'radius': radius
    }

    try:
        response = requests.get(f'{API_BASE_URL}/shopping/activities', params=params, headers=headers)
        response.raise_for_status()
        data = response.json()

        if 'data' not in data or not data['data']:
            return []

        # Calculate a safe random index based on available data
        data_length = len(data['data'])
        if data_length == 0:
            return []

        safe_max_index = min(max_index, data_length - 1)
        numb_rand = random.randint(0, safe_max_index)

        # Check if the selected data point has pictures
        if numb_rand >= data_length or 'pictures' not in data['data'][numb_rand]:
            return []

        pics = []
        for pic in data['data'][numb_rand]['pictures']:
            pics.append(pic)
            if len(pics) >= max_pics:
                break

        return pics
    except requests.exceptions.RequestException as e:
        print(f"API request error: {e}")
        return []
    except (KeyError, IndexError, ValueError) as e:
        print(f"Error processing response data: {e}")
        return []
    except Exception as e:
        print(f"Unexpected error: {e}")
        return []

def get_tokyo_pics(max_pics=DEFAULT_MAX_PICS):
    """API calls for Tokyo pictures"""
    return get_location_pics('35.710518', '139.797733', '20', 10, max_pics)

def get_rome_pics(max_pics=DEFAULT_MAX_PICS):
    """API calls for Rome pictures"""
    return get_location_pics('41.9028', '12.4964', '20', 8, max_pics)

def get_paris_pics(max_pics=DEFAULT_MAX_PICS):
    """API calls for Paris pictures"""
    return get_location_pics('48.8566', '2.3522', '20', 8, max_pics)

def get_dubai_pics(max_pics=DEFAULT_MAX_PICS):
    """API calls for Dubai pictures"""
    return get_location_pics('25.2048', '55.2708', '20', 4, max_pics)

def get_egypt_pics(max_pics=DEFAULT_MAX_PICS):
    """API calls for Egypt pictures"""
    return get_location_pics('29.9792', '31.1342', '20', 7, max_pics)
 
