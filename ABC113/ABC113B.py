#!/usr/bin/env python
# coding: utf-8

# In[20]:


N = int(input())
T,A = map(int,input().split())
List = list(map(int,input().split()))
div = 100000
for i in range(len(List)):
    heat = T - List[i] *0.006
    if(div>abs(A - heat)):
        div = abs(A -heat)
        ans = i + 1
print(ans)


# In[ ]:




