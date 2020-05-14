
# coding: utf-8

# In[5]:


N = int(input())
L = []
for i in range(N):
    a = int(input())
    if((a in L) == False):
        L.append(a)
L = sorted(L)
print(L[-2])

