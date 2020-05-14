
# coding: utf-8

# In[191]:


n,m = map(int,input().split())
radm = 360/60
rad_nm = 0.5
rad_nh = 30
if(n>=12):
    n -= 12
H = n*rad_nh + m*rad_nm
M = m * radm
ans = abs(H-M)
if(ans > 180):
    ans = 360 - ans
print(ans)

