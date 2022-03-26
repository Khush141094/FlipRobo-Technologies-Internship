#!/usr/bin/env python
# coding: utf-8

# In[41]:


import requests
from bs4 import BeautifulSoup
url = 'https://www.bewakoof.com/women-printed-tshirts'

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
products = soup.select('div.plp-product-card')
for product in products:
    name = product.select('h3')[0].text.strip()
    price = product.select('span.discountedPriceText ')[0].text.strip()
    image = product.select('img')[0].get('src')
    print(f'Product Name : {name}, Price : {price}, Image URL : {image} ')


# In[ ]:





# In[ ]:




