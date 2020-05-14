
# coding: utf-8

# In[57]:


N = int(input())
H = [int(input()) for i in range(N)]

L = [1]*N
R = [1]*N

for i in range(1,N):
    if H[i] > H[i-1]:
        L[i] = L[i-1] +1
    else:
        L[i] = 1

    if H[i] < H[i-1]:
        R[i] = R[i-1]+1
    else:
        R[i] = L[i]
print(max(R))

