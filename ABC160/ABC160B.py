
# coding: utf-8

# In[64]:


X = int(input())

ans = X//500 * 1000
X -= X//500 * 500
ans += X//5*5
print(ans)

