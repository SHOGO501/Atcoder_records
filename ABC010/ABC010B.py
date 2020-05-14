#!/usr/bin/env python
# coding: utf-8

# In[21]:


N = int(input())
a = list(map(int,input().split()))
ans = 0
for i in a:
    key = i%6
    if(key == 0):
        ans  += 3
    elif(key == 5):
        ans += 2
    elif(key == 2 or key == 4):
        ans += 1
    else:
        pass
print(ans)


# In[ ]:




