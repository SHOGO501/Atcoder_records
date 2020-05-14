#!/usr/bin/env python
# coding: utf-8

# In[29]:


N,T = map(int,input().split())
cost = 10000
ans = False
for i in range(N):
    c,t = map(int,input().split())
    if(T>=t and c < cost):
        cost = min(cost,c)
        ans = True
if(ans):
    print(cost)
else:
    print("TLE")


# In[ ]:




