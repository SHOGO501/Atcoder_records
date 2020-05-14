
# coding: utf-8

# In[62]:


L  = list(map(int,input().split()))
K = int(input())
L = sorted(L)
L[-1] = L[-1]*2**K
print(sum(L))

