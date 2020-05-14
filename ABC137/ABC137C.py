
# coding: utf-8

# In[15]:


import math
from collections import Counter

N = int(input())

L = []
for i in range(N):
    x = list(input())
    x.sort()
    x = "".join(x)
    L.append(x)


L = Counter(L)


def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

ans = 0
for i in L:
    a = L[i]
    if a > 1:
        ans += combinations_count(a,2)
print(ans)

