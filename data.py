import requests
from auth import get_auth  # import function


def get_data():
    access_token = get_auth()
    headers = {
        'Authorization': 'Bearer {TOKEN}'.format(TOKEN=access_token)
    }

    URL = 'https://api.spotify.com/v1/artists/{id}/top-tracks'.format(
        id='6M2wZ9GZgrQXHCFfjv46we')
    data = requests.get(URL + "?market=US", headers=headers)

    data = data.json()
    print(data)


if __name__ == '__main__':
    get_data()
