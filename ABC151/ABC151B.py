
# coding: utf-8

# In[21]:


N,K,M = map(int,input().split())
A = list(map(int,input().split()))
S = sum(A)
ans = True
for i in range(K+1):
    score = (S + i)/ N
    if score >= M:
        print(i)
        ans = False
        break
if ans:
    print(-1)


# In[22]:





# In[23]:




