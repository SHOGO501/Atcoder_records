
# coding: utf-8

# In[22]:


W,a,b = map(int,input().split())
if(abs(b-a) < W):
    print(0)
else:
    ans = abs(b - a) - W
    print(ans)

