
# coding: utf-8

# In[ ]:


A,B,C,K = map(int,input().split())
ans = 0

if A > K:
    ans = K
else:
    ans = A
    K -= A
    
    if B > K:
        pass
    else:
        K -= B
        ans -= K
        
print(ans)

