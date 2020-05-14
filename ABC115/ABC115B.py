#!/usr/bin/env python
# coding: utf-8

# In[30]:


N = int(input())
L = []
for i in range(N):
    s = int(input())
    L.append(s)
ans = sum(L) - max(L)/2
print(int(ans))


# In[ ]:




