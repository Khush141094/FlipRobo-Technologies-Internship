#!/usr/bin/env python
# coding: utf-8

# In[2]:


from bs4 import BeautifulSoup
import requests
import pandas as pd

page=requests.get("https://www.icc-cricket.com/rankings/womens/player-rankings/odi/all-rounder")
page

page.content


soup=BeautifulSoup(page.content,'html.parser')
soup


name=soup.find_all('div',class_="rankings-block__banner--name-large")
name

names=[]
for i in name:
    names.append(i.get_text())
names  


name=soup.find_all('td',class_="table-body__cell rankings-table__name name")
name[:9]


for i in name:
    names.append(i.get_text().replace('\n', ' '))
names[:10]    


team=soup.find_all('div',class_="rankings-block__banner--nationality")
team


teams=[]
for i in team:
    teams.append(i.get_text().replace('\n', ''))
teams   


team=soup.find_all('span',class_="table-body__logo-text")
team[:9]


for i in team:
    teams.append(i.get_text())
teams[:10]   


rating=soup.find_all('div',class_="rankings-block__banner--rating")
rating


ratings=[]
for i in rating:
    ratings.append(i.get_text())
ratings 


rating=soup.find_all('td',class_="table-body__cell rating")
rating[:9]


for i in rating:
    ratings.append(i.get_text())
ratings[:10] 


career_best=soup.find_all('span',class_="rankings-block__career-best-text")
career_best


career_best_rating=[]
for i in career_best:
    career_best_rating.append(i.get_text().replace('\n', ' ').replace('  ',''))
career_best_rating   


career_best=soup.find_all('td',class_="table-body__cell u-text-right u-hide-phablet")
career_best[:9]


for i in career_best:
    career_best_rating.append(i.get_text().replace('\n', ' ').replace('                        ',' '))
career_best_rating[:10]  



top10=pd.DataFrame({})
top10['Name']=names[:10]
top10['Team']=teams[:10]
top10['Rating']=ratings[:10]
top10['Career_best_rating']=career_best_rating[:10]


top10


# In[ ]:




