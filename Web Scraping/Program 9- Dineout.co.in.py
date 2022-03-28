#!/usr/bin/env python
# coding: utf-8

# In[76]:


import requests
from bs4 import BeautifulSoup

url = 'https://www.dineout.co.in/delhi-restaurants'

page = requests.get(url)
soup = BeautifulSoup(page.content,"html.parser")
restaurants = soup.select('div.restnt-detail-wrap')
for restaurant in restaurants:
    restaurant_name = restaurant.select('a')[0].text.strip()
    print(f'Restaurant Name : {restaurant_name}')
    restaurant_loc_1 = restaurant.select('a')[1].text.strip()
    restaurant_loc_2 = restaurant.select('a')[2].text.strip()
    print(f'Restaurant Location : {restaurant_loc_1}, {restaurant_loc_2}')
    restaurant_cusinies = restaurant.select('span')[0].select('a')
    cusinie_name= ''
    for i in range(len(restaurant_cusinies)):
        cusinie_name = cusinie_name + restaurant_cusinies[i].text.strip() + ','
    
    print(f'Restaurant Name : {restaurant_name}, Restaurant Location : {restaurant_loc_1}, {restaurant_loc_2}, Cusinie name : {cusinie_name}')
    
restaurants = soup.select('div.img-wrap')
for restaurant in restaurants:
    restaurant_rating = restaurant.select('div.restnt-rating')[0].text.strip()
    image = restaurant.select('img')[0].get('data-src')
    print(f'Restaurant Rating : {restaurant_rating}, Restaurant image : {image}')




            


# In[ ]:





# In[ ]:





# In[ ]:




