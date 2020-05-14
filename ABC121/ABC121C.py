
# coding: utf-8

# In[21]:


N,M = map(int,input().split())
L = []
for i in range(N):
    a,b = map(int,input().split())
    s = (a,b)
    L.append(s)
L.sort()
ans = 0
cnt = 0
for i,j in L:
    if(M> (cnt+ j)):
        ans += i * j
        cnt += j
    elif (M <= (cnt + j)):
        ans += i * (M - cnt)
        break
print(ans)

