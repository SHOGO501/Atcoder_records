#!/usr/bin/env python
# coding: utf-8

# In[36]:


K,S = map(int,input().split())
ans = 0
for i in range(K+1):
    for j in range(K+1):
        Z = S - i - j
        if(j>=0 and i>=0 and Z>=0 and K>=Z and S == i + j + Z):
            ans += 1
print(ans)

