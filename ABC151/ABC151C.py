
# coding: utf-8

# In[72]:


N,M = map(int,input().split())
AC = {}
WA = {}
for i in range(M):
    prb ,ans = input().split()
    if ans == "AC":
        AC[prb] = 1
    else:
        if (prb in WA) == False and (prb in AC) ==  False:
            WA[prb] = 1
        else:
            if (prb in AC) ==  False:
                WA[prb] +=1
wa = 0
for i,v in WA.items():
    if (i in AC):
        wa += v
print("{} {}".format(len(AC),wa))


# In[73]:


WA


# In[75]:


("2" in AC)

