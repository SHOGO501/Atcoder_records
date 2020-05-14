
# coding: utf-8

# In[1]:


n,X = map(int,input().split())
a = list(map(int,input().split()))
S = ""
while(X >= 1):
    if(X % 2 == 0):
        S = "0" + S
        X /= 2
    else:
        S = "1" + S
        X //= 2
ans = 0
for i in range(len(S)):
    j = -(i + 1)
    if(S[j] == "1"):
           ans += a[i]
print(ans)

