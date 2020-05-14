
# coding: utf-8

# In[1]:


txa,tya,txb,tyb,T,V = map(int,input().split())

from math import sqrt

def dis(x1,y1,x2,y2):
    return sqrt((x2-x1)**2 + (y2-y1)**2)

n = int(input())
for i in range(n):
    a,b = map(int,input().split())
    time = dis(txa,tya,a,b) + dis(a,b,txb,tyb)
    if T * V >= time:
        print("YES")
        quit()
        
print("NO")

