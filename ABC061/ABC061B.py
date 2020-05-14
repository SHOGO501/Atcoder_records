
# coding: utf-8

# In[58]:


N,M = map(int,input().split())
dic = {}
for i in range(1,N+1):
    dic[i] = 0
for i in range(M):
    a,b = map(int,input().split())
    dic[a] += 1
    dic[b] += 1
for key,value in dic.items():
    print(value)


# In[53]:





# In[57]:




