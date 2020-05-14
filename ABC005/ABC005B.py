
# coding: utf-8

# In[25]:


N = int(input())
ans = 1000000
for i in range(N):
    s = int(input())
    ans = min(s,ans)
print(ans)

