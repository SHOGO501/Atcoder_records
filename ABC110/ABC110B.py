#!/usr/bin/env python
# coding: utf-8

# In[46]:


N,M,X,Y = map(int,input().split())
xi = sorted(list(map(int,input().split())))
yi = sorted(list(map(int,input().split())))
Z = yi[0]
if(Z>xi[-1] and Z >X and Z <= Y):
    print("No War")
else:
    print("War")


# In[ ]:




