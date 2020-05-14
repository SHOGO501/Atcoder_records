
# coding: utf-8

# In[20]:


A,B = map(int,input().split())
S = input()
ans = True
for i in range(len(S)):
    if(i == A):
        if(S[i] != "-"):
            ans = False
    else:
        if(S[i].isdigit() != True):
            ans = False
if(len(S) != A + B + 1):
    ans = True
if(ans):
    print("Yes")
else:
    print("No")

