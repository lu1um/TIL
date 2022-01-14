#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup

url = f'https://maple.gg/u/알바생최현진'
response = requests.get(url).text
data = BeautifulSoup(response, 'html.parser')
exchange = data.select_one('#user-profile > section > div.row.row-normal > div.col-lg-8 > div.user-summary > ul > li:nth-child(1)')
result = exchange.text

print('알바생최현진의 레벨은 ' + result + '입니다.')
