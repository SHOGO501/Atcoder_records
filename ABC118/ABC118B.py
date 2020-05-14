#!/usr/bin/env python
# coding: utf-8

# In[1]:


N,M = map(int,input().split())
dic = {}
for i in range(N):
    a = list(map(int,input().split()))
    a = a[1:]
    for j in a:
        if(j in dic):
            dic[j] += 1
        else:
            dic[j] = 1


# In[4]:


ans = 0
for key,value in dic.items():
    if(value == N):
        ans += 1
print(ans)


# In[ ]:




