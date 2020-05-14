
# coding: utf-8

# In[58]:


A,B,C,D = map(int,input().split())
ans = 0
alice = [i for i in range(A,B+1)]
bob = [i for i in range(C,D+1)]
for i in alice:
    if(i in bob):
        ans += 1
print(max((ans - 1),0))

