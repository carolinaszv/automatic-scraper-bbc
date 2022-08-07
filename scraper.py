#!/usr/bin/env python
# coding: utf-8

# # Automatic scraper
# Let's Fucking Goooooo

# In[1]:


import requests
from bs4 import BeautifulSoup


# In[3]:


response= requests.get("https://www.bbc.com")
doc = BeautifulSoup(response.text)


# In[7]:


#Grab all of the titles
titles = doc.select(".media__title")
titles


# In[10]:


for title in titles:
    print(title.text.strip())


# In[11]:


# We want linkssss so let's redo
titles = doc.select(".media__title a")
titles


# In[13]:


for title in titles:
    print(title.text.strip())
    print(title['href'])


# In[15]:


import pandas as pd

#Start with an empty list
rows = []

for title in titles:
    # Go through each title, building a dictionary
    # with a 'title' and a 'url'
    row ={}
    
    # title
    row['title'] = title.text.strip()
    # link
    row['link'] = title['href']
    
    # Then add it to our list of rows
    rows.append(row)

# then we're going to create a dataframe from it!!! (Go back and import pandas!)
df = pd.DataFrame(rows)
df


# In[16]:


df.to_csv("bbc.csv", index=False)


# In[ ]:





# In[ ]:




