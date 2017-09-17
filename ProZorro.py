
# coding: utf-8


import requests
import json


response = requests.get('https://lb.api.openprocurement.org/api/0/tenders/ae5ccc2b1a974a80a294f21190dbd7ed')
# print(response.content)
result = json.loads(response.content)
# Если раскоментировать строку ниже, можно смотреть ключи
# print result
# Вместо ['data']['procuringEntity']['name'] нужно вписать паравильные ключи словаря 
print(result['data']['procuringEntity']['name'])
