
# coding: utf-8

# In[69]:


N,M,C = map(int,input().split())


# In[70]:


B = list(map(int,input().split()))


# In[73]:


A = []
for i in range(N):
    s = list(map(int,input().split()))
    A.append(s)


# In[79]:


ans = 0
for i in A:
    cnt = 0
    for j in range(M):
        cnt += i[j]*B[j]
    if cnt > -C:
        ans+=1


# In[80]:


ans

