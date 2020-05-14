
# coding: utf-8

# In[10]:


S = input()
ans = ""
for i in S:
    if i == "0":
        ans += "0"
    elif i == "1":
        ans += "1"
    else:
        if len(ans) != 0:
            ans = ans[:-1]
print(ans)

