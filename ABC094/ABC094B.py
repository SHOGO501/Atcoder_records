
# coding: utf-8

# In[1]:


N,M,X = map(int,input().split())
L = list(map(int,input().split()))
over = 0
lower = 0
for i in L:
    if(i < X):
        lower += 1
    else:
        over += 1
ans = min(over,lower)
print(ans)

