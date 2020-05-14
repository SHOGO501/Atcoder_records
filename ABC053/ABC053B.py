
# coding: utf-8

# In[13]:


S = input()
for i in range(len(S)):
    if(S[i]== "A"):
        a = i
        break
for i in reversed(range(len(S))):
    if(S[i] == "Z"):
        z = i
        break
az = S[a:z]
print(len(az)+1)

