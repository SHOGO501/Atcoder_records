
# coding: utf-8

# In[102]:


A,B,K = map(int,input().split())


# In[104]:


cnt = 0
for i in reversed(range(1,min(A,B)+1)):
    if(A%i==0 and B%i == 0):
        cnt+=1
        if(cnt == K):
            print(i)

