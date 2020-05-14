#!/usr/bin/env python
# coding: utf-8

# In[6]:


N,K = map(int,input().split())
ans = 0
for i in range(1,N+1):
    if(i < K):
        point = i
        count = 0
        while(point < K):
            count += 1
            point *= 2
        ans += (1/N)*(1/2)**count
    else:
        ans += (1/N)
print(ans)


# In[ ]:




