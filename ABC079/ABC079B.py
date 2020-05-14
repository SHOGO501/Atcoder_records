#!/usr/bin/env python
# coding: utf-8

# In[7]:


N = int(input())
luca = [2,1]
cnt = 2
while(cnt <= N):
    L = luca[cnt - 2] + luca[cnt - 1]
    luca.append(L)
    cnt += 1
print(luca[N])


# In[ ]:




