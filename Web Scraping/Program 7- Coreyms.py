#!/usr/bin/env python
# coding: utf-8

# In[18]:


import requests
from bs4 import BeautifulSoup

url = 'https://coreyms.com/'

page = requests.get(url)
soup = BeautifulSoup(page.content,"html.parser")
articles = soup.select('article')

for i in range(len(articles)):
    headers = soup.select('header.entry-header')
    article_heading = headers[i].select('h2')[0].text.strip()
    article_date = headers[i].select('time')[0].text.strip()
    
    contents = soup.select('div.entry-content')
    article_content = contents[i].select('p')[0].text.strip()
    
    youtube_url = soup.select('iframe')[0].get('src')
    
    print(f'Article heading : {article_heading}')
    print(f'Article date : {article_date}')
    print(f'Article content : {article_content}')
    print(f'Youtube URL : {youtube_url}')
    print('******************************************************************************************')
    


# In[ ]:





# In[ ]:




