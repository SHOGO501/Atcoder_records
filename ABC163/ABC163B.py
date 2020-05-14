
# coding: utf-8

# In[3]:


N,M = map(int,input().split())
A = list(map(int,input().split()))

ans = N - sum(A)
if sum(A) > N:
    print(-1)
else:
    print(ans)
    

