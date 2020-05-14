
# coding: utf-8

# In[5]:


N = int(input())
mod = 1000000007
ans = 1
for i in range(1,N+1):
    ans = (i * ans)%mod
print(ans)

