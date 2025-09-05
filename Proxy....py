import requests

proxy = {
    'http': 'http://username:password@proxyserver:port',
    'https': 'https://username:password@proxyserver:port'
}

try:
    response = requests.get('http://example.com', proxies=proxy)
    print(response.text)  
except requests.exceptions.RequestException as e:
    print(f"Ошибка: {e}")
 // add

AEYpXvDN7C
