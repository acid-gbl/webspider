#!/usr/bin/env python
# coding: utf-8

# In[34]:


import os
import requests
import json

def download(img_url, file_name, file_path='./img'):
    if not os.path.isdir(file_path):
        os.mkdir(file_path)
    file_suffix = os.path.splitext(img_url)[1]
    dir = file_path + '/' + file_name + file_suffix
    try:
        pic = requests.get(img_url)
        fp = open(dir, 'wb')
        fp.write(pic.content)
        fp.close()
    except requests.exceptions.ConnectionError:
        print('Sorrry,image cannot downloaded, url is error{}.'.format(img_url))
        
def getHTMLText(ulr):
    try:
        headers = { 'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'  ,
                        'Referer':'http://www.baidu.com/' } 
        r=requests.get(url,timeout=30,headers=headers)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return ""

# 这个url比较特殊，直接用源代码
agisurl = "https://www.bilibili.com/activity/web/view/data/814?csrf=68af6c61bc4f65f034c6ee8e6403af85"
r = requests.get(agisurl)
decoded = json.loads(r.text)
decoded


# In[13]:


import requests
import re
from bs4 import BeautifulSoup

def getHTMLText(ulr):
    try:
        headers = { 'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'  ,
                        'Referer':'http://www.baidu.com/' } 
        r=requests.get(url,timeout=30,headers=headers)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return ""


# In[11]:


import pandas as pd
up_info=[]
details = decoded['data']['list']
colnames=['index', 'name', 'uid', 'description']
for dd in range(len(details)):
    # download images
    # download('http:' + details[dd]['data']['face'], file_name=str(dd).rjust(3,'0') + '-' + details[dd]['name'])
    up_info.append((str(dd).rjust(3,'0'),details[dd]['name'],details[dd]['data']['uid'],details[dd]['data']['desc']))


# In[12]:


data=pd.DataFrame(up_info,columns=colnames)
data


# In[36]:


up_url='https://space.bilibili.com/116683/fans/follow'
r = getHTMLText(up_url)
from bs4 import BeautifulSoup
soup=BeautifulSoup(r)
# console.warn('log-reporter.js加载失败，放弃上报')应该是js动态页面？？用json解析？？


# In[22]:


followers_list=soup.find_all("ul",{"class":"content"})
followers_info=[]
followers_list

