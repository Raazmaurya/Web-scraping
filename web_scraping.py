#!/usr/bin/env python
# coding: utf-8

# In[4]:


import urllib.request
from bs4 import BeautifulSoup as bs
import re
import pandas as pd
# loads html code from a url
page = urllib.request.urlopen("https://docs.python.org/3/library/random.html")
soup = bs(page)

# find all function names
names = soup.body.findAll('dt')
function_names = re.findall('id="random.\w+', str(names))
function_names = [item[4:] for item in function_names]

# find all function descriptions
description = soup.body.findAll('dd')
function_usage = []

for item in description:
    item = item.text
    item = item.replace('\n', ' ')
    function_usage.append(item)

print('list of function names:', function_names[:5])
print('\nfunction description:', function_usage[0])
print('\nnumber of items in function names:', len(function_names))#to check 
print('number of items in function description:', len(function_usage))#to check 
# create a dataframe  using pandas
data = pd.DataFrame({'function name': function_names,
                    'function usage': function_usage})
data.head()


# In[ ]:




