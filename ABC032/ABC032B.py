
# coding: utf-8

# In[124]:


S = input()
k = int(input())
dic = {}
for i in range(len(S) -(k-1)):
    a = S[i:i+k]
    if((a in dic) == False):
        dic[a] = 0
    else:
        dic[a] += 1
print(len(dic))

