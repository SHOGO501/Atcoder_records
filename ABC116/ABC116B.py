#!/usr/bin/env python
# coding: utf-8

# In[29]:


s = int(input())
L = [s]
cnt = 1
f = s
while(True):
    cnt += 1
    if(f % 2 == 0):
        f = f / 2
    else:
        f = 3 * f + 1
    if(f in L):
        print(cnt)
        break
    else:
        L.append(f)


# In[ ]:




