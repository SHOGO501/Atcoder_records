#!/usr/bin/env python
# coding: utf-8

# In[8]:


import sys
read = sys.stdin.buffer.read#全部読み込むやつ
readline = sys.stdin.buffer.readline#1行読み込むやつ
readlines = sys.stdin.buffer.readlines#リストで読み込むらしい

N,K,*H = map(int,read().split())
N -= K
if N <= 0:
    print(0)
    exit()
    
H.sort()
    
print(sum(H[:N]))


# In[ ]:




