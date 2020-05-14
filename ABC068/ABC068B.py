
# coding: utf-8

# In[73]:


N = int(input())
ans = 1
while(True):
    ans *= 2
    if(ans > N):
        print(ans//2)
        break

