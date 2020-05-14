#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
read = sys.stdin.buffer.read#全部読み込むやつ
readline = sys.stdin.buffer.readline#1行読み込むやつ
readlines = sys.stdin.buffer.readlines#リストで読み込むらしい

import math
H,A = map(int,read().split())
ans = math.ceil(H/A)
print(ans)


# In[ ]:




