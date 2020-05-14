
# coding: utf-8

# In[72]:


import itertools
import math
n = int(input())
s = []
for i in range(n):
    x,y = map(int,input().split())
    s.append([x,y])
s = list(itertools.permutations(s))
ans = 0
for i in s:
    for j in range(n-1):
        ans += math.sqrt((i[j][0] - i[j+1][0])**2 + (i[j][1] - i[j+1][1])**2)
print(ans/len(s))

