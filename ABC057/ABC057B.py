
# coding: utf-8

# In[70]:


N,M = map(int,input().split())
ab = []
for i in range(N):
    a,b = map(int,input().split())
    ab.append((a,b))
cd = []
for i in range(M):
    c,d = map(int,input().split())
    cd.append((c,d))
ans = []
for i in range(len(ab)):
    aaa = 1000000000
    for j in range(len(cd)):
        man = abs(ab[i][0] - cd[j][0]) + abs(ab[i][1] - cd[j][1])
        if(man < aaa):
            aaa = man
            cnt = j + 1
    ans.append(cnt)
for i in ans:
    print(i)


# In[74]:




