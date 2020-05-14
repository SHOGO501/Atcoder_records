
# coding: utf-8

# In[ ]:


N,M,X = map(int,input().split())

L = [list(map(int,input().split()))  for i in range(N)]

cost = 10**12

import itertools

S = list(itertools.product([0,1],repeat=N))


for i in S:
    cnt = 0
    ablity = [0] * M
    for j in range(N):
        if i[j] == 1:
            for k in range(M+1):
                if k == 0:
                    cnt += L[j][k]
                    
                else:
                    ablity[k-1] += L[j][k]
    
    ans = True
    for i in ablity:
        if i < X:
            ans = False
    
    if ans:
        cost = min(cost,cnt)
        
if cost == 10**12:
    print(-1)
else:
    print(cost)

