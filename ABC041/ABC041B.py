
# coding: utf-8

# In[32]:


A,B,C = map(int,input().split())
mod = 10**9 + 7
ans = (A*B*C) % mod
print(ans)

