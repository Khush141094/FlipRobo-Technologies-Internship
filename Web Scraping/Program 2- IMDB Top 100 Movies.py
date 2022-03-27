#!/usr/bin/env python
# coding: utf-8

# In[5]:


from bs4 import BeautifulSoup
import requests

page=requests.get("https://www.imdb.com/search/title/?count=100&groups=top_100&sort=user_rating")
page

page.content

soup=BeautifulSoup(page.content,'html.parser')
soup

names=soup.find_all('h3',class_="lister-item-header")
names[0:10]

movies=[]  
for i in names:
    for j in i.find_all('a'):
        movies.append(j.text)
movies[0:10]            

rating=soup.find_all('strong')
rating[0:10]

ratings=[]   
for i in rating:
    ratings.append(i.get_text().replace('Detailed', " ").replace('User Rating', " "))
ratings[:10]    

year=soup.find_all('span',class_="lister-item-year text-muted unbold")
year[0:10]

release_year=[]  
for i in year:
    release_year.append(i.get_text().replace('(I) ', " "))
release_year[:10]


import pandas as pd
IMDB_100=pd.DataFrame({})
IMDB_100['Movie_name']=movies
IMDB_100['Rating']=ratings[2:]
IMDB_100['Year_of_Release']=release_year


IMDB_100


# In[ ]:




