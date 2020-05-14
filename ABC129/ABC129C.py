
# coding: utf-8

# In[101]:


N,M =map(int,input().split())
a = [int(input()) for i in range(M)]
DP = [1]*N
mod = 10**9 + 7
for i in a:
    DP[i-1] = 0
if(N != 1):
    for i in range(N):
        if(DP[i] != 0):
            if(i<1):
                DP[i] = DP[i-1]%mod
            else:
                DP[i] = (DP[i-2] + DP[i-1])%mod
else:
    DP = [1]
print(DP[-1])

