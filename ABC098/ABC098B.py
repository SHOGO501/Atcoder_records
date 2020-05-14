
# coding: utf-8

# In[36]:


N = int(input())
S = input()
ans = 0
for i in range(1,len(S)):
    X = S[:i]
    Y = S[i:]
    dic = {}
    for j in X:
        if( (j in Y) == True):
            dic[j] = 0
        ans = max(ans,len(dic))
print(ans)


# In[33]:




