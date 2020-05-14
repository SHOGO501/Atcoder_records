
# coding: utf-8

# In[9]:


import itertools
L = map(int,input().split())
A =  list(itertools.combinations(L,3))
ans = []
for i,j,k in A:
    a = i + j + k
    ans.append(a)
ans.sort()
m = max(ans)
cnt = 1
for i in reversed(ans):
    if i < m:
        m = i
        cnt += 1
    if cnt == 3:
        print(i)
        break


# In[10]:





# In[18]:




