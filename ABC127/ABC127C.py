
# coding: utf-8

# In[17]:


import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


# In[13]:


N,M =map(int,input().split())
left = 0
right = 10**5 + 1
for i in range(M):
    l,r = map(int,input().split())
    left = max(l,left)
    right = min(r,right)
ans = right - left + 1
if(right - left < 0):
    ans = 0
print(ans)


# In[11]:





# In[12]:




