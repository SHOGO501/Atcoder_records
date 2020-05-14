
# coding: utf-8

# In[72]:


N,X = map(int,input().split())
L = []
for i in range(N):
    m = int(input())
    L.append(m)
X -= sum(L)
ans = N + X//min(L)
print(ans)

