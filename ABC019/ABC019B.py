
# coding: utf-8

# In[57]:


S = input()
ans = ""
first = S[0]
word = S[0]
j = 1
while(j < len(S)):
    if(first == S[j]):
        word += S[j]
    else:
        ans += word[0] + str(len(word))
        first = S[j]
        word = S[j]
    j += 1
ans += word[0] + str(len(word))
print(ans)

