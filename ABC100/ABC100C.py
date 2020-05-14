
# coding: utf-8

# In[ ]:


n = int(input())
A = list(map(int,input().split()))

ans = 0
for i in A:
    b =i
    if b%2 == 0:
        while(True):
            if b %2 == 0:
                b /= 2
                ans+=1
            else:
                break
print(ans)

