#!/usr/bin/env python
# coding: utf-8

# In[8]:


N = int(input())
L = list(map(int,input().split()))
L =sorted(L)
print(abs(L[-1] - L[0]))

