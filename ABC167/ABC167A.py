
# coding: utf-8

# In[ ]:


S = input()
T = input()

flag = True
for i in range(len(S)):
    if S[i] == T[i]:
        pass
    else:
        flag = False
        
if flag:
    print("Yes")
else:
    print("No")

