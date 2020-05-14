
# coding: utf-8

# In[50]:


N,A,B = map(int,input().split())
ans = 0
for i in range(N):
    s,d = input().split()
    d = int(d)
    if(d < A):
        d = A
    elif(B<d):
        d = B
    if(s == "East"):
        ans += d
    else:
        ans -= d
if(ans > 0):
    print("{} {}".format("East",ans))
elif(ans < 0):
    print("{} {}".format("West",-ans))
else:
    print(0)

