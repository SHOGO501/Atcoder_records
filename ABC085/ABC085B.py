
# coding: utf-8

# In[12]:


N = int(input())
L = []
for i in range(N):
    a = int(input())
    L.append(a)
L = sorted(L)
ans = 0
cnt = 0
for i in L:
    if(i > cnt):
        cnt = i
        ans += 1
print(ans)

