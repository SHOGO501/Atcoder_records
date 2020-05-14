
# coding: utf-8

# In[2]:


N,K = map(int,input().split())
A = list(map(int,input().split()))

cnt = 0
dic = {1:0}
x = 1
for i in range(N):
    y = A[x-1]
    cnt += 1
    if y in dic:
        x = y        
        break
    else:
        dic[y] = cnt
        x = y

    if cnt == K:
        print(y)
        quit()
       
loop = (K-dic[x]) % (cnt - dic[x])

for i in range(loop):
    x = A[x-1]
print(x)

