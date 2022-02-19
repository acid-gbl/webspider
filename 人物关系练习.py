#!/usr/bin/env python
# coding: utf-8

# In[4]:


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


# **<font size=6 color=blue>只爬取第一页</font>**

# In[15]:


start_url='https://www.tvmao.com/drama/YmdkYW4p/episode'
i=2
url=start_url+'/'+str(int(i/3))+'-'+str(i)

html=getHTMLText(url)
print(html)


# In[16]:


soup=BeautifulSoup(html)
print(soup)


# In[17]:


article = soup.find('article', {'class': 'clear epi_c'})
epi_list = article.findChildren("p")
epi_info=[]
epi_list[0].text


# In[18]:


for i in epi_list:
    epi_info.append(i.text)
epi_info


# **<font size=6 color=blue>尝试翻页</font>**其实就是观察翻页之后，*url*的变化规律

# In[24]:


infoList=[]
depth=31 #翻页的次数
for i in range(depth):
    try:
        url=start_url+'/'+str(int(i/3))+'-'+str(i)
        html=getHTMLText(url)
        soup=BeautifulSoup(html)
        article = soup.find('article', {'class': 'clear epi_c'})
        epi_list = article.findChildren("p")
        for i in epi_list:
            infoList.append(i.text)
    except:
        continue
infoList


# In[26]:


import pandas as pd
infoMat=pd.DataFrame(infoList,columns=['剧集情节'])
infoMat


# In[23]:


with pd.ExcelWriter('人物关系.xlsx') as writer:
      infoMat.to_excel(writer, sheet_name='data',encoding="gbk")

