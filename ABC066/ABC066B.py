
# coding: utf-8

# In[22]:


S = input()
S = S[:len(S)-1]
while(True):
    A = S[:int(len(S)/2)]
    B = S[int(len(S)/2):]
    if(A == B):
        print(len(S))
        break
    S = S[:len(S)-1]

