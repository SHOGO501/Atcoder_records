#!/usr/bin/env python
# coding: utf-8

# In[4]:


N = int(input())
K = int(input())
ans = 1
for i in range(N):
    ans = min(ans*2,ans+K)
print(ans)


# In[ ]:




