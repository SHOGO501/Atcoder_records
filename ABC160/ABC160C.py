
# coding: utf-8

# In[78]:


N,K = map(int,input().split())
S = list(map(int,input().split()))

D = [0] * K

for i in range(K-1):
    D[i] = S[i+1] - S[i]

D[-1] = (N - S[-1]) +S[0]
print(sum(D) - max(D))

