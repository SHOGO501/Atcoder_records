#!/usr/bin/env python
# coding: utf-8

# In[5]:


S = input()
T = input()
leng = len(S)
ans = False

for i in range(leng):
    if(S == T):
        ans = True
    S = S[-1] + S[0:-1]
if(ans):
    print("Yes")
else:
    print("No")


# In[ ]:




