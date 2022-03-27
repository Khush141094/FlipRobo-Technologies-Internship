#!/usr/bin/env python
# coding: utf-8

# In[2]:


from bs4 import BeautifulSoup
import requests
import pandas as pd

page=requests.get("https://www.icc-cricket.com/rankings/mens/team-rankings/odi")
page

page.content

soup=BeautifulSoup(page.content,'html.parser')
soup

team=soup.find_all('span',class_="u-hide-phablet")
team[:10]

teams=[] 
for i in team:
    teams.append(i.get_text())
teams[:10]

match=soup.find_all('td',class_="rankings-block__banner--matches")
match

Matches=[]  
for i in match:
    Matches.append(i.get_text().replace('\n',''))
Matches

match=soup.find_all('td',class_="table-body__cell u-center-text")
match[:9]

del match[1::2]   

for i in match:
    Matches.append(i.get_text().replace('\n',''))
Matches[:10]

points=soup.find_all('td',class_="rankings-block__banner--points")
points

Points=[]  
for i in points:
    Points.append(i.get_text().replace('\n',''))
Points

points=soup.find_all('td',class_="table-body__cell u-center-text")
points[:9]

del points[::2]  

for i in points:
    Points.append(i.get_text().replace('\n',''))
Points[:10]

rating=soup.find_all('td',class_="rankings-block__banner--rating u-text-right")
rating

Rating=[]  
for i in rating:
    Rating.append(i.get_text().replace('\n','').strip())
Rating

rating=soup.find_all('td',attrs={'class':'table-body__cell u-text-right rating'})
rating[:9]

for i in rating:
    Rating.append(i.get_text().replace('\n',''))
Rating=Rating[0:10]  
Rating


Team_Rankings=pd.DataFrame({})
Team_Rankings['Team']=teams[:10]
Team_Rankings['Matches']=Matches[:10]
Team_Rankings['Points']=Points[:10]
Team_Rankings['Rating']=Rating

Team_Rankings

