
# coding: utf-8

# In[9]:


N = int(input())
dic = {}
for i in range(N):
    s = input()
    if((s in dic) == False):
        dic[s] = 1
    else:
        dic[s] +=1
key = 0
for i,j in dic.items():
    if(j>key):
        key = j
        ans = i
print(ans)

