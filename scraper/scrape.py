import requests
def fetch_data():
    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': 'e4ef08a3-ed6d-48ca-8791-03d749bf78df',
    }
    params = {
    'start':'1',
    'limit':'100',
    'convert':'USD'
    }
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
    resp = requests.get(url,headers=headers,params=params)
    data = dict(resp.json())['data']
    return data


