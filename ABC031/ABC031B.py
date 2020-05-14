
# coding: utf-8

# In[130]:


L,H = map(int,input().split())
N = int(input())
for i in range(N):
    A = int(input())
    if(L<= A and A <= H):
        print(0)
    elif(H<A):
        print(-1)
    else:
        print(L-A)

