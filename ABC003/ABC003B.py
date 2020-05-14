
# coding: utf-8

# In[30]:


S = input()
T = input()
ans = True
for i in range(len(S)):
    if(S[i] == T[i]):
        pass
    elif(S[i] == "@" and (T[i] in "atcoder")):
         pass
    elif(T[i] == "@" and (S[i] in "atcoder")):
         pass
    else:
        ans = False
if(ans):
    print("You can win")
else:
    print("You will lose")

