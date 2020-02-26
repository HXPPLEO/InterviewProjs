#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pypinyin import pinyin, lazy_pinyin, Style
import pandas as pd
import random


# In[2]:


def getcitylastname(x):
    '''得到城市名的尾字拼音'''
    city_lastname = lazy_pinyin(x)[-1]
    return city_lastname


# In[3]:


def nextcities(x,y):
    '''得到一个可接城市的list'''
    return [city for city in y if getcitylastname(x) == lazy_pinyin(city)[0]]


# In[13]:


def game(number):
    '''正式游戏，参数number是接龙次数'''
    print('Loading game...')
    china_city_array = pd.read_html('https://github.com/wangx404/city_demino/blob/master/city_list.txt')[0][1].values #中国城市和地方名
    
    print('游戏开始了')
    next_city = input('请输入一个城市或地名：')
    while number > 0:
        city_list = nextcities(next_city ,china_city_array)
        if len(city_list) == 0:
            print('下面没有了')
            break
        else:
            next_city = random.choice(city_list)
            print('下一个城市是：',next_city)
        number -= 1
        if number == 0:
            print('已经跑完了')


# In[15]:


game(10)


# In[ ]:




