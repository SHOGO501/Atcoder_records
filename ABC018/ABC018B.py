
# coding: utf-8

# In[87]:


S = input()
N = int(input())
for i in range(N):
    l,r = map(int,input().split())
    s = S[l-1:r]
    s = s[::-1]
    S = S[:l-1] + s +S[r:]
print(S)

