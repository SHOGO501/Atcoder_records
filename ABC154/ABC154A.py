#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
read = sys.stdin.buffer.read#全部読み込むやつ
readline = sys.stdin.buffer.readline#1行読み込むやつ
readlines = sys.stdin.buffer.readlines#リストで読み込むらしい


# In[1]:


S,T = input().split()
A,B = map(int,input().split())
U = input()

if U == S:
    A -= 1
else:
    B -=1
    
print("{} {}".format(A,B))


# In[19]:




