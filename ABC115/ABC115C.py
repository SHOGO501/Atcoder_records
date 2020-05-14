
# coding: utf-8

# In[12]:


N,K=map(int,input().split())
L = [int(input()) for i in range(N)]

L.sort()
ans = 10**12
for i in range(N-K+1):
    A = L[i]
    B = L[i+K-1]
    ans = min(ans,B-A)
print(ans)

