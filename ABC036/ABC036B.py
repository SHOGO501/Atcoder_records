
# coding: utf-8

# In[39]:


N = int(input())
L = []
for i in range(N):
    s = input()
    L.append(s)
ans = []
for i in range(N):
    a = ""
    for j in reversed(range(len(L))):
        a += L[j][i]
    ans.append(a)
for i in ans:
    print(i)

