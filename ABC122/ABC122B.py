
# coding: utf-8

# In[64]:


S = input()


# In[65]:


ans = 0
List = ["A","C","G","T"]
cnt = 0
for i in S:
    if(i in List):
        cnt += 1
        ans = max(ans,cnt)
    else:
        cnt = 0


# In[66]:


print(ans)


# In[41]:




