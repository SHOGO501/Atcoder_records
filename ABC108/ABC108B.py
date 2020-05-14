
# coding: utf-8

# In[1]:


x1,y1,x2,y2 = map(int,input().split())


# In[2]:


x = x2 - x1
y = y2 - y1


# In[3]:


x3 = x2 - y
y3 = y2 + x
x4 = x1 - y
y4 =y1 + x


# In[4]:


print("{} {} {} {}".format(x3,y3,x4,y4))

