
# coding: utf-8

# In[64]:


S = input()
T = input()
ans = ""
for i in range(len(T)):
    ans += S[i]
    ans += T[i]
if(len(S)>len(T)):
    ans += S[-1]
print(ans)

