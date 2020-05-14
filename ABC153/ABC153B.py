#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
read = sys.stdin.buffer.read#全部読み込むやつ
readline = sys.stdin.buffer.readline#1行読み込むやつ
readlines = sys.stdin.buffer.readlines#リストで読み込むらしい

H,N,*A = map(int,read().split())
S = sum(A)
if H <= S:
    print("Yes")
else:
    print("No")

