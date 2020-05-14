
# coding: utf-8

# In[25]:


m = int(input())
if(m<100):
    print("00")
elif(m <= 5000):
    ans = int(m / 100)
    if(ans < 10):
        ans = "0" + str(ans)
        print(ans)
    else:
        print(ans)
elif(m <= 30000):
    ans = m/1000 + 50
    print(int(int(ans)))
elif(m <= 70000):
    ans = int((m/1000 - 30)/5+80)
    print(ans)
else:
    print(89)


# In[12]:




