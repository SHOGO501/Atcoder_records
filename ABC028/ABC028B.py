
# coding: utf-8

# In[4]:


from collections import Counter

s = input() + "ABCDEF"
C = Counter(s)
ANS = []
for key in sorted(C.keys()):
    ANS.append(str(C[key]-1))
print(" ".join(ANS))

