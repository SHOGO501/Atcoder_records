
# coding: utf-8

# In[1]:


w = input()
dic = {}
for i in w:
    if(i in dic) == False:
        dic[i] = 1
    else:
        dic[i] += 1
ans = True
for key,value in dic.items():
    if(value %2 == 0):
        continue
    else:
        ans = False
        break
if(ans):
    print("Yes")
else:
    print("No")

