import requests

url = 'https://jable.tv/search/%E4%BC%8A%E8%97%A4%E8%88%9E%E9%9B%AA/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36'}

response = requests.get(url, headers=headers)
if response.status_code == 200:
    data = response
    print(data)
else:
    print('error')