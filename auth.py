import os
import requests  # allows for http requests to be made
from dotenv import load_dotenv, find_dotenv


load_dotenv()

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')

AUTH_URL = 'https://accounts.spotify.com/api/token'


def get_auth():

    auth_response = requests.post(AUTH_URL, {
        'grant_type': 'client_credentials',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
    })

    print(auth_response)  # 200 response is good, 400 something broke

    auth_response_data = auth_response.json()

    access_token = auth_response_data['access_token']

    return access_token


if __name__ == "__main__":
    token = get_auth()
