#!/usr/bin/env python
# coding: utf-8

# In[4]:


N = int(input())
ans = 0
for i in range(N):
    x,u = input().split()
    
    if(u == "JPY"):
        ans += int(x)
    else:
        ans += float(x)*380000
print(ans)


# In[ ]:




