
# coding: utf-8

# In[28]:


import copy
N = int(input())
T = list(map(int,input().split()))
M = int(input())
P = []
for i in range(M):
    p,x = map(int,input().split())
    P.append([p,x])
ans = sum(T)
for i in P:
    X = copy.copy(T)
    X[i[0]-1] = i[1]
    ans = sum(X)
    print(ans)


# In[27]:


T


# In[26]:


X[3]=1

