
# coding: utf-8

# In[68]:


N = int(input())
dic = {}
for i in range(N):
    a = int(input())
    if((a in dic) == False):
        dic[a] = 1
    else:
        dic[a] += 1
ans = 0
for key,value in dic.items():
    if(value>1):
        ans += value - 1
print(ans)

