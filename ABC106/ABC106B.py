#!/usr/bin/env python
# coding: utf-8

# In[5]:


N = int(input())
ans = 0
for i in range(1,N+1,2):
    count = 0
    for j in range(1,i+1):
        if(i%j == 0):
            count += 1
    if(count == 8):
        ans += 1
print(ans)


# In[6]:





# In[ ]:




