#!/usr/bin/env python
# coding: utf-8

# In[12]:


N = int(input())
M = N
S = 0
while(M>0):
    S += M%10
    M /= 10
    M = int(M)
if(N%S == 0):
    print("Yes")
else:
    print("No")


# In[ ]:




