
# coding: utf-8

# In[49]:


import math
N = int(input())
L = []
for i in range(N):
    r = int(input())
    L.append(r)
L = sorted(L)
ans = 0
cnt = 1
for i in reversed(range(N)):
    if(cnt%2 != 0):
        ans += (L[i]**2)*math.pi
    else:
        ans -= (L[i]**2) * math.pi
    cnt += 1
print(ans)

