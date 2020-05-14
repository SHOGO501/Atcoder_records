
# coding: utf-8

# In[29]:


N = int(input())
X = N
fx = 0
while(N>0):
    fx += N%10
    N = N//10
if(X % fx == 0):
    print("Yes")
else:
    print("No")

