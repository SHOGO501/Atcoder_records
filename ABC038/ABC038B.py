
# coding: utf-8

# In[92]:


H1,W1 = map(int,input().split())
H2,W2 = map(int,input().split())
ans = False
if(H1 == H2 or H1 == W2 or H2 == W1 or W1 == W2):
    ans = True
if(ans):
    print("YES")
else:
    print("NO")

