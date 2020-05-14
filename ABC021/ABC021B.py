
# coding: utf-8

# In[80]:


N = int(input())
dic = {}
a,b = map(int,input().split())
K = int(input())
dic[a] = 1
dic[b] = 1
List = list(map(int,input().split()))
ans = True
for i in List:
    if((i in dic) == False):
        dic[i] = 1
    else:
        ans = False
        break
if(ans):
    print("YES")
else:
    print("NO")

