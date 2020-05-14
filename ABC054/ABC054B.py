#!/usr/bin/env python
# coding: utf-8

# In[78]:


N,M = map(int,input().split())
S = [input() for _ in range(N)]
T = [input() for _ in range(M)]
ans = False
cnt = N - M
for i in range(cnt+1):
    for j in range(cnt + 1):
        tmp = T[0]
        check = S[i][j:M+j]
        key = 0
        if(check == tmp):
            key += 1
            for k in range(1,M):
                tmp = T[k]
                check =  S[i+k][j:M+j]
                if(check == tmp):
                    key += 1
        if(key == M):
            ans =True
            break

if(ans):
    print("Yes")
else:
    print("No")

