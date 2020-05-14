#!/usr/bin/env python
# coding: utf-8

# In[19]:


W,H,N = map(int,input().split())
zero = [0,0]
X = [W,H]
ans = True
for i in range(N):
    x,y,a = map(int,input().split())
    if(a == 1):
        if zero[0] < x < X[0]:
            zero[0] = x
        elif X[0] <= x:
            ans = False
            break
    elif(a == 2):
        if zero[0] < x < X[0]:
            X[0] = x
        elif zero[0] >= x:
            ans = False
            break
    elif(a == 3):
        if zero[1] < y < X[1]:
            zero[1] = y
        elif X[1] <= y:
            ans = False
            break
    elif(a == 4):
        if zero[1] < y < X[1]:
            X[1] = y
        elif zero[1] >= y:
            ans = False
            break
if(ans):
    S = (X[1] - zero[1]) * (X[0] - zero[0])
    print(S)
else:
    print(0)


# In[ ]:




