
# coding: utf-8

# In[22]:


N = int(input())
L = [0,0,1]
for i in range(N):
    S = sum(L[i:i+3])%10007
    L.append(S)
print(L[N-1])

