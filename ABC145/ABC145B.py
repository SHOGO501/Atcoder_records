
# coding: utf-8

# In[72]:


n = int(input())
s = input()
s = sorted(s)
ans = True
if(len(s)>1 and len(s)%2 == 0):
    for i in range(0,len(s),2):
        if(s[i] != s[i+1]):
            ans = False
else:
    ans = False
if(ans):
    print("Yes")
else:
    print("No")

