#!/usr/bin/env python
# coding: utf-8

# In[25]:


N = int(input())
H = list(map(int,input().split()))
DP = [0]
for i in range(1,N):
    if(i == 1):
        DP.append(abs(H[i]-H[i-1]))
    else:
        DP.append(min(abs(H[i]-H[i-1])+DP[i-1],abs(H[i] - H[i-2])+DP[i-2]))
print(DP[-1])

