
# coding: utf-8

# In[6]:


N = int(input())
ans = 0
for i in range(N):
    l,r = map(int,input().split())
    ans += r - l + 1
print(ans)

