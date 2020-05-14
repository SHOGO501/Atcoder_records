
# coding: utf-8

# In[44]:


N,M = map(int,input().split())
A = list(map(int,input().split()))

X = sum(A)/(4*M)
ans = 0

for i in A:
    if not (i < X):
        ans += 1

if ans >=M:
    print("Yes")
else:
    print("No")

