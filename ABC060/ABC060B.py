
# coding: utf-8

# In[61]:


A,B,C = map(int,input().split())
ans = False
for i in range(1,1000):
    K = i * A
    if(K % B == C):
        ans = True
        break
if(ans):
    print("YES")
else:
    print("NO")

