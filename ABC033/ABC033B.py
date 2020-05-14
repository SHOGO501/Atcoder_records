
# coding: utf-8

# In[116]:


n = int(input())
cnt = 0
dic = {}
for i in range(n):
    s,t = input().split()
    t = int(t)
    cnt += t
    dic[s] = t
ans = "atcoder"
for key,value in dic.items():
    if(value > cnt/2):
        ans = key
print(ans)

