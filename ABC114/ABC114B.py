#!/usr/bin/env python
# coding: utf-8

# In[8]:


S = input()
ans = 753
for i in range(len(S)):
    A = int(S[i:i+3])
    ans = min(ans,abs(753 - A))
print(ans)


# In[ ]:




