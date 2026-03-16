#https://tryscrapeme.com/web-scraping-practice/beginner/post

import requests
import sys
from lxml import etree

def fetch_html() -> str:
    url = 'https://tryscrapeme.com/web-scraping-practice/beginner/post'
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36'}
    payload = {'query':'tryscrapeme'}
    response = requests.post(url, headers=headers, data=payload)
    if response.status_code != 200:
        print('Error code: ', response.status_code)
        sys.exit(1)
    return response.text

html = fetch_html()
root = etree.HTML(html)
lst = []
trs = root.xpath('//tr')
for tr in trs:
    tds = tr.xpath('./td')
    if len(tds) >= 4:
        s = tds[3].text
        if s != '':
            print(s)
            price = float(s)
            lst.append(price)
total = sum(lst)
print(total)
