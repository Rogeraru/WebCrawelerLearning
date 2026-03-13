# https://tryscrapeme.com/web-scraping-practice/beginner/abc

import requests
import sys
from lxml import etree

url = 'https://tryscrapeme.com/web-scraping-practice/beginner/abc'
try:
    response = requests.get(url)
except requests.exceptions.RequestException as e:
    print(f"failed to fetch {url} : {e}")
    sys.exit(1)

if response.status_code != 200:
    print(f"failed to fetch {url} ,status code: {response.status_code}")
    sys.exit(1)

html = response.text
root = etree.HTML(html)
lst = []

trs = root.xpath('//tr') #從整個文件往下找
for tr in trs:
    tds = tr.xpath('./td') #只從當前節點往下找
    if len(tds) >= 4:
        price = tds[3].text
        if price != "":
            price = float(price)
            lst.append(price)
ans = sum(lst)
print(ans)
