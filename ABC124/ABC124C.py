#!/usr/bin/env python
# coding: utf-8

# In[ ]:


S = input()
ans_0 = 0
ans_1 = 0
check = "0"
for i in S:
    if i == check:
        ans_0 += 1
    else:
        ans_1 += 1
    
    if check == "0":
        check = "1"
    else:
        check = "0"
print(min(ans_0,ans_1))


# In[ ]:




