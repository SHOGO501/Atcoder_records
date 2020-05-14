#!/usr/bin/env python
# coding: utf-8

# In[9]:


import sys
read = sys.stdin.buffer.read#全部読み込むやつ
readline = sys.stdin.buffer.readline#1行読み込むやつ
readlines = sys.stdin.buffer.readlines#リストで読み込むらしい

S = read().rstrip()
length = len(S)
ans = "x" * length
print(ans)


# In[ ]:




