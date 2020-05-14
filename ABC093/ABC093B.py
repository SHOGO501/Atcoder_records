
# coding: utf-8

# In[19]:


A,B,K = map(int,input().split())
List = []
for i in range(K):
    c = A + i
    d = B - i
    if((c in List) == False and c >= A and c <= B):
        List.append(c)
    if((d in List) == False and d >= A and d <= B):
        List.append(d)
List = sorted(List)
for i in List:
    print(i)

