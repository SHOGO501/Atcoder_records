#!/usr/bin/env python
# coding: utf-8

# In[14]:


N = int(input())
ans = False
for i in range(100):
    for j in range(100):
        total = 4 * i + 7 * j
        if(total == N):
            ans = True
            break
if(ans):
    print("Yes")
else:
    print("No")


# In[ ]:




