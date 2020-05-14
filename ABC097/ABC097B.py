
# coding: utf-8

# In[48]:


X =int(input())
ans = 0
for i in range(1,X+1):
    for j in range(2,11):
        A = i ** j
        if(A<=X):
            ans = max(ans,A)
print(ans)

