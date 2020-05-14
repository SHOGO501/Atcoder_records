
# coding: utf-8

# In[5]:


a,b = map(int,input().split())
if (b == 100):
    AB = a * 1000 + b
elif(b > 9):
    AB = a * 100 + b
else:
    AB = a * 10 + b
cnt = 1
ans = False
while(True):
    x = cnt * cnt
    if(x == AB):
        ans = True
    if(x > AB):
        break
    cnt += 1
if(ans):
    print("Yes")
else:
    print("No")

