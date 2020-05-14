
# coding: utf-8

# In[31]:


A,B,C = map(int,input().split())
prass = False
mainas = False
if(A+B == C):
    prass = True
    
if(A-B == C):
    mainas = True

if(prass and mainas):
    print("?")
elif(prass):
    print("+")
elif(mainas):
    print("-")
else:
    print("!")

