import requests

def list_all (type_output):
    url = 'https://rest.coinapi.io/v1/{}'.format(type_output)
    headers = {'X-CoinAPI-Key': '74C5EF15-91AB-430C-8CBA-3B0505EECFB8'}
    response = requests.get(url, headers=headers)
    return response.json()