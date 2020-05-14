
# coding: utf-8

# In[ ]:


N = int(input())
A = [0]*5
A[0] = int(input())
A[1] = int(input())
A[2] = int(input())
A[3] = int(input())
A[4] = int(input())
nekku = min(A)
ans = N//nekku + 4
if N%nekku != 0:
    ans += 1
print(ans)

