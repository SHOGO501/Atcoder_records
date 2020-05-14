#!/usr/bin/env python
# coding: utf-8

# In[4]:


import sys
read = sys.stdin.buffer.read#全部読み込むやつ
readline = sys.stdin.buffer.readline#1行読み込むやつ
readlines = sys.stdin.buffer.readlines#リストで読み込むらしい

N = readline()
A = list(map(int,readline().split()))

setA = len(set(A))


        
if setA == len(A):
    print("YES")
else:
    print("NO")


# In[ ]:




