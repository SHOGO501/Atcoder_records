
# coding: utf-8

# In[67]:


N = int(input())
S = input()
juery = "b"
ans = False
for i in range(1,1+N):
    if(juery == S):
        ans = True
        a = 0
        break
    if(i%3==0):
        juery = "b" + juery + "b"
    elif(i%3 == 1):
        juery = "a" + juery + "c"
    else:
        juery = "c" + juery + "a"
    if(juery == S):
        ans = True
        a = i
        break
if(ans):
    print(a)
else:
    print(-1)


# In[60]:




