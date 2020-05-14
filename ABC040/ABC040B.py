
# coding: utf-8

# In[84]:


n = int(input())
ans = 10**9
for i in range(1,n+1):
    a = i
    b = n//i
    mod = n % a
    ans = min(ans,abs(a-b)+mod)
print(ans)

