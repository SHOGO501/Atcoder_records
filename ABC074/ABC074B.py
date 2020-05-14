
# coding: utf-8

# In[5]:


N = int(input())
K = int(input())
xi = list(map(int,input().split()))
ans = 0
for i in xi:
    ans += min(i,abs(K - i)) *2
print(ans)

