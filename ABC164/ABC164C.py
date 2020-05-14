
# coding: utf-8

# In[ ]:


from collections import Counter

N = int(input())
L = []
for i in range(N):
    L.append(input())
    
X = Counter(L)
print(len(X))

