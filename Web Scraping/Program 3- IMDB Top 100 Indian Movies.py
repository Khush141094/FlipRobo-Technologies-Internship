#!/usr/bin/env python
# coding: utf-8

# In[3]:


from bs4 import BeautifulSoup
import requests
import pandas as pd

page=requests.get("https://www.imdb.com/india/top-rated-indian-movies/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=461131e5-5af0-4e50-bee2-223fad1e00ca&pf_rd_r=KW9XY49QFKX5SR23QR6F&pf_rd_s=center-1&pf_rd_t=60601&pf_rd_i=india.toprated&ref_=fea_india_ss_toprated_india_tr_india250_hd")
page

page.content

soup=BeautifulSoup(page.content,'html.parser')
soup

names=soup.find_all('td',class_='titleColumn')
names[0:10]

movies=[]
for i in names:
    for j in i.find_all('a'):   
        movies.append(j.text)
movies[0:10]  

ratings=soup.find_all('strong')
ratings[0:10]


rating=[] 
for i in ratings:
    rating.append(i.get_text())
rating[:10]    

year=soup.find_all('span',class_="secondaryInfo")
year[0:10]

release_year=[]  
for i in year:
    release_year.append(i.get_text())
release_year[:10]


IMDB_Indian100=pd.DataFrame({})
IMDB_Indian100['Movie_name']=movies[:100]
IMDB_Indian100['Rating']=rating[:100]
IMDB_Indian100['Year_of_Release']=release_year[:100]

IMDB_Indian100


# In[ ]:




