
# coding: utf-8

# In[ ]:


N = int(input())
L = [tuple(map(int,input().split())) for i in range(N)]
X = sorted(L, key = lambda k:k[1])
cnt = 0
ans = True
for i,j in X:
    cnt += i
    if cnt > j:
        ans = False
        break
        
if ans:
    print("Yes")
else:
    print("No")

