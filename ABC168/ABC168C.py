
# coding: utf-8

# In[1]:


import math
A,B,H,M = map(int,input().split())
rad = abs(M/60 * 360 - ((H + M/60)/12)*360)
c = A**2 + B**2 - 2*A*B*math.cos(math.radians(rad))
print(math.sqrt(c))

