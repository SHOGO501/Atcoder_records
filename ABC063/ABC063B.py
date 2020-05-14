
# coding: utf-8

# In[33]:


S = input()
dic = {}
ans = True
for i in S:
    if((i in dic) == False):
        dic[i] = 1
    else:
        ans = False
        break
if(ans):
    print("yes")
else:
    print("no")

