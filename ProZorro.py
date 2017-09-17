
# coding: utf-8

# In[3]:


import requests
import json
response = requests.get('http://api-docs.openprocurement.org/uk_UA/latest/')
print(response.content)

