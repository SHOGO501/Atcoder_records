
# coding: utf-8

# In[17]:


A,B,X = map(int,input().split())
left = 0
right = X + 1
mid = (left + right) //2

while(right - left >1):
    ans = A * mid + B * len(str(mid))
    if(ans < X):
        left = mid
    else:
        right = mid
    mid = (left + right)//2
    
ans = A * right + B * len(str(right))
if(left > 10**9):
    ans = 10 **9
elif(ans <= X):
    ans = right
else:
    ans = left
print(ans)

