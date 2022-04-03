#!/usr/bin/env python
# coding: utf-8

# In[19]:


import requests
from bs4 import BeautifulSoup
url = 'https://www.nobroker.in/property/sale/hyderabad/multiple?searchParam=W3sibGF0IjoxNy40NDc0NDc1LCJsb24iOjc4LjM1NjkyNzUsInBsYWNlSWQiOiJDaElKZzVwcF9KU1R5enNSaHBYNzU2M2VkX2ciLCJwbGFjZU5hbWUiOiJJbmRpcmEgTmFnYXIifSx7ImxhdCI6MTcuNTAwMDcyOCwibG9uIjo3OC40MDUxOTU5OTk5OTk5OSwicGxhY2VJZCI6IkNoSUpzWEZxb3VtUnl6c1JiWlZ5ZGVqMkdKSSIsInBsYWNlTmFtZSI6IkpheWFuYWdhciBDb2xvbnkifV0=&radius=2.0&city=hyderabad&locality=Indira%20Nagar,&locality=Jayanagar%20Colony'

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
houses = soup.select('article')
for house in houses:
    house_name = house.select('h2')[0].text.strip()
    house_area = house.select('#minRent')[0].text.strip()
    house_emi = house.select('#roomType')[0].text.strip()
    house_price = house.select('#minDeposit')[0].text.strip()
    print(f'House name : {house_name}, Area : {house_area}, EMI : {house_emi}, Price : {house_price}')


# In[ ]:




