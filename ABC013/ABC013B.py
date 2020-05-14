
# coding: utf-8

# In[ ]:


a = int(input())
b = int(input())
ans = min([abs(a-b),abs(b+10-a),abs(a-b+10)])
print(ans)

