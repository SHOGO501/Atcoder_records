
# coding: utf-8

# In[45]:


import math
N = int(input())
L = list(map(int,input().split()))
S = len(L)
for i in L:
    if(i == 0):
        S -= 1
ans = math.ceil(sum(L)/S)
print(int(ans))

