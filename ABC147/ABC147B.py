
# coding: utf-8

# In[22]:


S = input()
cnt = len(S)//2
ans = 0
for i in range(cnt):
    if S[i] !=  S[-i-1]:
        ans += 1
print(ans)


# In[24]:




