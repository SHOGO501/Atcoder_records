
# coding: utf-8

# In[16]:


L1 = [7,8,9,0]
L2 = [4,5,6]
L3 = [2,3]
L4 = [1]
Lx = [L1,L2,L3,L4]

a,b = map(int,input().split())

def check(L,num,s):
    if num in L:
        L[L.index(num)] = s 

def cehck2(L):
    for i,v in enumerate(L):
        if type(v) == int:
            L[i] = "x"
    print(*L)
        
s = "."
for i in range(2):
    L = list(map(int,input().split()))
    for j in L:
        for k in Lx:
            check(k,j,s)
    s = "o"
    
for i in Lx:
    cehck2(i)

