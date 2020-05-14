#!/usr/bin/env python
# coding: utf-8

# In[11]:


D,N = map(int,input().split())
ans = (100**D) * N
if(N == 100):
    ans +=  100**D
print(ans)


# In[ ]:




