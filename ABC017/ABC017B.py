
# coding: utf-8

# In[94]:


X = input()
i = 0
ans = True
while(i < len(X)):
    S = X[i]
    if(S == "o" or S == "k" or S == "u"):
        pass
    elif(S == "c"):
        if(X[i+1] == "h"):
            i += 1
        else:
            ans = False
            break
    else:
        ans = False
        break
    i += 1
if(ans):
    print("YES")
else:
    print("NO")

