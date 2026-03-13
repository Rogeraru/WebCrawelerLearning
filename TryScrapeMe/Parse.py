#https://tryscrapeme.com/web-scraping-practice/beginner/parse

import requests
import sys

from lxml import etree

url = 'https://tryscrapeme.com/web-scraping-practice/beginner/parse'

try:
    response = requests.get(url)
except requests.exception.RequestException as e:
    print(f'failed with exception {e}')
    sys.exit()

if response.status_code != 200:
    print(f'failed with status code {response.status_code}')
    sys.exit()

html = response.text
root = etree.HTML(html)

#Dom:
# <tr>
#     <td><h4>The Brain That Changes Itself</h4></td>
#     <td>Norman Doidge</td>
#     <td>4</td>
#     <td><span>$</span>11.03</td>
# </tr>

lst = []
body = root.xpath('//tbody')

for tbody in body:
    trs = tbody.xpath('./tr')
    for tr in trs:
        target = tr.xpath('./td[4]/text()')
        price = float(target[0])
        lst.append(price)
total_price = sum(lst)
print(f'total price is {total_price}')
