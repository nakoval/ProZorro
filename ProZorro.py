
# coding: utf-8

# In[3]:


import requests
import json
response = requests.get('http://api-docs.openprocurement.org/uk_UA/latest/')
print(response.content)
result = json.loads(response.json)[0]
# Вместо ['data']['item'][...] нужно вписать паравильные ключи словаря 
print(result['data'])

