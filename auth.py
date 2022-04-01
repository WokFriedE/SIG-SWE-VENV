import os
import requests
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())  # Loads .env file
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
AUTH_URL = "https://accounts.spotify.com/api/token"


def get_auth():

    auth_response = requests.post(AUTH_URL, {
        'grant_type': 'client_credentials',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
    })

    print(auth_response)  # 200 response is good

    auth_response_data = auth_response.json()
    print(auth_response_data)

    token = auth_response_data['access_token']

    print(token)
    return token


if __name__ == "__main__":
    get_auth()