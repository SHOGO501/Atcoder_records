
# coding: utf-8

# In[ ]:


N = int(input())
words = []
s = input()
words.append(s)
ans = True
for i in range(N-1):
    t = input()
    if(t[0] == s[-1] and (t in words) == False):
        words.append(t)
        s = t
    else:
        ans = False
if(ans):
    print("Yes")
else:
    print("No")

