
# coding: utf-8

# In[3]:


N,K = map(int,input().split())
L = list(map(int,input().split()))
L = sorted(L)
ans = sum(L[len(L)- K :])
print(ans)

