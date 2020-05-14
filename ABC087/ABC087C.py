
# coding: utf-8

# In[50]:


N = int(input())
L1 = list(map(int,input().split()))
L2 = list(map(int,input().split()))
ans= 0
for i in range(N):
    s = sum(L1[:i+1]) + sum(L2[i:])
    ans = max(ans,s)
print(ans)

