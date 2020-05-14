
# coding: utf-8

# In[ ]:


N = int(input())
S = input()

all = S.count("R") * S.count("G") * S.count("B")
count = 0
for i in range(N):
    for j in range(1,N):
        k = 2*j - i
        if k < N and i < j:
            if (S[i] != S[j]) and (S[j] != S[k]) and (S[k] != S[i]):
                count += 1
print(all-count)    

