
# coding: utf-8

# In[7]:


N,Q = map(int,input().split())
S = input()
T = [0]*(N+1)
for i in range(N):
    T[i+1] = T[i] + (1 if S[i : i + 2] == "AC" else 0)
for i in range(Q):
    l,r = map(int,input().split())
    print(T[r-1] - T[l-1])

