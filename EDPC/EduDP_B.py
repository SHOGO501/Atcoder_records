
# coding: utf-8

# In[31]:


N,k=map(int,input().split())
h = list(map(int,input().split()))
DP = [0] * N
for i in range(1,N):
    dp = [0] * (k)
    for j in range(1,k+1):
        if(i - j) >=0:
            dp[j-1] = abs(h[i] - h[i-j]) + DP[i-j]
        else:
            dp[j-1] = 10**6
    DP[i] = min(dp)
print(DP[-1])

