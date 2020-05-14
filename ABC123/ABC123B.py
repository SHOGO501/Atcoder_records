
# coding: utf-8

# In[44]:


List= [int(input()) for i in range(5)]


# In[54]:


amari =9
time = 0
flag = False;
for i in List:
    if(i%10 != 0):
        time += 10 - i%10
        amari = min(amari,i%10)
        flag = True


# In[55]:


output = sum(List) + time
if(flag):
    output -= 10 - amari
print(output)


# In[42]:


amari


# In[41]:


time

