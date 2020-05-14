#!/usr/bin/env python
# coding: utf-8

# In[ ]:


N = int(input())
DP = [[0]*3]*N
abc = [0] * N
for i in range(N):
    L = list(map(int,input().split()))
    abc[i] = L
for i,value in enumerate(abc):
    dp = [0]*3
    for j in range(3):
        for k in range(3):
            if j != k:
                dp[k] = max(dp[k],DP[i-1][j] + value[k])
    DP[i] = dp
print(max(DP[-1]))


# In[ ]:


#maspy ansewr
import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N = int(readline())
m = map(int,read().split())
ABC = zip(m,m,m)

x,y,z = 0,0,0 # 最後の活動 -> 幸福度のmax
for a,b,c in ABC:
    x,y,z = max(y,z)+a,max(x,z)+b,max(x,y)+c

answer = max(x,y,z)
print(answer)

