
# coding: utf-8

# In[3]:


import requests
import json
response = requests.get('https://lb.api.openprocurement.org/api/0/tenders/ae5ccc2b1a974a80a294f21190dbd7ed')
print(response.content)
result = json.loads(response.json)[0]
# Вместо ['data']['item'][...] нужно вписать паравильные ключи словаря 
print(result['data'])

