#!/usr/bin/env python
# coding: utf-8

# 模拟浏览器输入及点击

# In[1]:


from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

#headless
#chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument('--headless')
#chrome_options.add_argument('--disable-gpu')
#driver = webdriver.chrome(chrome_options=chrome_options)

#head
driver = webdriver.Chrome()

driver.get("https://www.taobao.com/")
driver.find_element_by_xpath("//a[@class='h']").click()


# In[2]:


#登录
driver.find_element_by_id("fm-login-id").clear()
driver.find_element_by_id("fm-login-id").send_keys("")
driver.find_element_by_id("fm-login-password").clear()
driver.find_element_by_id("fm-login-password").send_keys("")

#手动滑块验证（因为暂时还不知道怎么用代码拖滑块）


# In[3]:


driver.find_element_by_xpath("//button[@class='fm-button fm-submit password-login']").click()
#可能出现协议更新
#driver.find_element_by_xpath("//button[@class='btn btn-large']").click()


# In[1]:


good="笔记本"
driver.find_element_by_id("q").clear()
driver.find_element_by_id("q").send_keys(good)
driver.find_element_by_xpath("//button[@class='btn-search tb-bg']").click()


# In[11]:


goods_list=[]
depth=5
for i in range(depth):
    goods_name=driver.find_elements_by_xpath("//a[@class='J_ClickStat']")
    goods_price=driver.find_elements_by_xpath("//div[@class='price g_price g_price-highlight']")
    for i in range(len(goods_name)):
        goods_list.append([goods_name[i].text,goods_price[i].text])
    driver.find_element_by_xpath("//li[@class='item next']").click()
    time.sleep(5)


# 输出商品表格

# In[12]:


tplt="{:4}\t{:8}\t{:16}"
print(tplt.format("序号","价格","商品名称"))
count=0
for g in goods_list:
    count=count+1
    print(tplt.format(count,g[1],g[0]))

