
# coding: utf-8

# In[8]:


S = input()


# In[10]:


S = input()
string = [chr(i) for i in range(97, 97+26)]


# In[18]:


S = input()
string = [chr(i) for i in range(97, 97+26)]
ans = True
for i in string:
    if((i in S) == False):
        print(i)
        ans = False
        break
if(ans):
    print("None")

