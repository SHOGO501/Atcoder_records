
# coding: utf-8

# In[25]:


L = []
for i in range(4):
    s = list(input().split())
    s = s[::-1]
    L.append(s)
for i in reversed(range(4)):
    print(*L[i])

