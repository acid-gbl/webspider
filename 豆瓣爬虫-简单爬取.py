#!/usr/bin/env python
# coding: utf-8

# In[1]:


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

# In[17]:


start_url='https://movie.douban.com/top250'
url=start_url
html=getHTMLText(url)
print(html)


# In[18]:


soup=BeautifulSoup(html)
print(soup)


# In[77]:


movie_list=soup.find_all("div",{"class":"info"})
movie_info=[]
movie_list[1]


# In[78]:


for i in movie_list:
    title=i.find("span", {"class":"title"}).text
    rating=i.find("span", {"class":"rating_num"}).text
    inq=i.find("span", {"class":"inq"}).text
    movie_info.append((title,rating,inq))
import pandas as pd
colnames=['标题','评分','简评']
data=pd.DataFrame(movie_info,columns=colnames)
data


# In[79]:


data.to_csv('D:\python练手\webspider\豆瓣爬虫数据.csv',encoding="gbk")


# **<font size=6 color=blue>尝试翻页</font>**其实就是观察翻页之后，*url*的变化规律

# In[111]:


infoList=[]
depth=8 #翻页的次数
for i in range(depth):
    try:
        url=start_url+'?start='+str(25*i)
        html=getHTMLText(url)
        soup=BeautifulSoup(html)
        movie_list=soup.find_all("div",{"class":"info"})
        for i in movie_list:
            title=i.find("span", {"class":"title"}).text
            rating=i.find("span", {"class":"rating_num"}).text
            inq=i.find("span", {"class":"inq"}).text
            infoList.append((title,rating,inq))
    except:
        continue
import pandas as pd
colnames=['标题','评分','简评']
longdata=pd.DataFrame(infoList,columns=colnames)
longdata


# In[ ]:


longdata.to_csv('D:\python练手\webspider\豆瓣爬虫数据.csv',encoding="gbk")

