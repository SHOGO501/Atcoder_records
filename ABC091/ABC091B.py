
# coding: utf-8

# In[10]:


N = int(input())
S = {}
for i in range(N):
    j = input()
    if((j in S) == False):
        S[j] = 1
    else:
        S[j] += 1
M = int(input())
T = {}
for i in range(M):
    j = input()
    if((j in T) == False):
        T[j] = 1
    else:
        T[j] += 1
ans = 0
for key,value in S.items():
    if(key in T):
        ans = max(ans,value - T[key])
    else:
        ans = max(ans,value)
print(ans)


# In[14]:


ans

