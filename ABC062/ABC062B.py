
# coding: utf-8

# In[35]:


H,W = map(int,input().split())
ans = ["#" * (W+2)]
for i in range(H):
    S = input()
    S = "#" + S + "#"
    ans.append(S)
ans.append("#" * (W+2))
for i in ans:
    print(i)

