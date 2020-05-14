
# coding: utf-8

# In[15]:


N,L = map(int,input().split())
S = []
for i in range(N):
    s = input()
    S.append(s)
S = sorted(S)
ans = ""
for i in S:
    ans += i
print(ans)

