
# coding: utf-8

# In[27]:


N = int(input())
dic = {}
for i in range(1,N+1):
    bi = int(input())
    dic[i] = bi
botan = 1
cnt = 0
while(True):
    botan = dic[botan]
    cnt += 1
    if(botan == 2):
        print(cnt)
        break
    if(cnt > N):
        print(-1)
        break

