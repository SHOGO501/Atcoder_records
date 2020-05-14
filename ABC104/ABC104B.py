
# coding: utf-8

# In[23]:


S = input()
ans = False
if(S[0]=="A" and S[2:len(S)-1].find("C") != -1 and S.count("C") == 1):
    S = S.replace("C","c")
    ans = S[1:].islower()
if(ans):
    print("AC")
else:
    print("WA")

