#!/usr/bin/env python
# coding: utf-8

# In[28]:


import sys
read = sys.stdin.buffer.read#全部読み込むやつ
readline = sys.stdin.buffer.readline#1行読み込むやつ
readlines = sys.stdin.buffer.readlines#リストで読み込むらしい


N,*L = map(int,read().split())
ans = 0
Pj = L[0]
for i in L:
    Pj = min(Pj,i)    
    if Pj >= i:
        ans += 1
print(ans)


# In[31]:





# In[ ]:




