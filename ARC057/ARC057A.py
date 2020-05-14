
# coding: utf-8

# In[15]:


A,K = map(int,input().split())
oder = 2 * 1000000000000
t = 0

if K == 0:
    print(oder - A)
    quit()

while(True):
    if A >= oder:
        break
    A += K * A +1
    t += 1
print(t)

