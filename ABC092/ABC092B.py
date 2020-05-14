
# coding: utf-8

# In[7]:


N = int(input())
D,X = map(int,input().split())
L = []
for i in range(N):
    a = int(input())
    L.append(a)
ans = N + X
for i in L:
    cnt = 1
    while(True):
        A = cnt * i + 1
        if(A <= D):
            ans += 1
        else :
            break
        cnt += 1
print(ans)


# In[4]:




