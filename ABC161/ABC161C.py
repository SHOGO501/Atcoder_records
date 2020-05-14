
# coding: utf-8

# In[48]:


n,k = map(int,input().split())
t = n%k
ans = min(t,abs(t-k))
print(ans)


# In[ ]:




