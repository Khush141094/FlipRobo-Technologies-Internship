#!/usr/bin/env python
# coding: utf-8

# In[24]:


import requests
from bs4 import BeautifulSoup
url = 'https://meesho.com/bags-ladies/pl/p7vbp'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
products= soup.find_all('div',class_="sc-dkzDqf ProductList__GridCol-sc-8lnc8o-0 kmfTGq ZnDzz")
for product in products:
    name = product.select('p')[0].text.strip()
    price = product.select('h5')[0].text.strip()
    discount = product.select('span')[0].text.strip()
    print(f'Product name : {name}, Product price : {price}, Product discount : {discount}')


# In[ ]:





# In[ ]:




