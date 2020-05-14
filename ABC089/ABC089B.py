
# coding: utf-8

# In[5]:


N = int(input())
ans = False
s = list(input().split())
for i in s:
    if(i == "Y"):
        ans = True
if(ans):
    print("Four")
else:
    print("Three")

