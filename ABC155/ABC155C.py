#!/usr/bin/env python
# coding: utf-8

# In[28]:


import sys
read = sys.stdin.buffer.read#全部読み込むやつ
readline = sys.stdin.buffer.readline#1行読み込むやつ
readlines = sys.stdin.buffer.readlines#リストで読み込むらしい


# In[22]:


N = int(input())

dic = {}

for i in range(N):
    S = input()
    
    if (S in dic) == False:
        dic[S] = 1
    else:
        dic[S] += 1
        
keys = []
maxv = max(dic.values())
for key , value in dic.items():
    if value == maxv:
        keys.append(key)
k = keys.sort()
for i in keys:
    print(i)


# In[ ]:




