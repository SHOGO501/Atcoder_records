
# coding: utf-8

# In[37]:


N,K = map(int,input().split())
ans = K * (K-1)**(N-1)
print(ans)

