
# coding: utf-8

# In[33]:


N = int(input())
S = input()
ans = ""
for i in S:
    tmp = ord(i)
    tmp += N
    if(tmp>90):
        tmp -= 26
    ans += chr(tmp)
print(ans)

