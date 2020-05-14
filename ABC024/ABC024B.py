
# coding: utf-8

# In[51]:


N,T = map(int,input().split())
time = 0
ans = 0
L = []
for i in range(N):
    t = int(input())
    L.append(t)
for i in range(N-1):
    back = L[i]
    now = L[i+1]
    div = now -back
    if(div>T):
        ans += T
    else:
        ans += div
ans += T
print(ans)

