#!/usr/bin/env python
# coding: utf-8

# In[6]:


N = int(input())
List = list(map(int,input().split()))


# In[13]:


List = sorted(List)
s = sum(List) - List[-1]


# In[15]:


if(List[-1]<s):
    print("Yes")
else:
    print("No")


# In[ ]:




