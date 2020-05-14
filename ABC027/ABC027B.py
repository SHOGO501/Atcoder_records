#!/usr/bin/env python
# coding: utf-8

# In[ ]:


N = int(input())
A = list(map(int,input().split()))
ans = 0
if sum(A)%N != 0:
    ans = -1
else:
    if sum(A) == 0:
        ans = 0
    else:
        check = sum(A)/N
        amari = 0
        for i in range(len(A)):
            amari = A[i] - check + amari
            if amari != 0:
                ans += 1
print(ans)

