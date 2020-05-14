
# coding: utf-8

# In[5]:


A,B = map(int,input().split())
ans = 0
for i in range(A,B+1):
    S = str(i)
    if(S[0] == S[4] and S[1] == S[3]):
        ans += 1
print(ans)

