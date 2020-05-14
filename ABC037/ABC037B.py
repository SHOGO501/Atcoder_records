
# coding: utf-8

# In[3]:


N,Q = map(int,input().split())
L = [0]* N
for i in range(Q):
    l,r,t = map(int,input().split())
    A = [t]*(r-l+1)
    L[l-1:r] = A
for i in L:
    print(i)

