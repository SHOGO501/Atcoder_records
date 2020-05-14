
# coding: utf-8

# In[2]:


S = input()
N = int(input())

for i in range(min(N,len(S))):
    if S[i] != "1":
        print(S[i])
        quit()

print(1)

