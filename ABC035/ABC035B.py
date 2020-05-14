
# coding: utf-8

# In[102]:


S = input()
T = int(input())
def manhattan(x):
    man = abs(x[0]) + abs(x[1])
    return man
def man(x,maxma):
    x1 = [x[0] + 1,x[1]]
    x2 = [x[0] -1,x[1]]
    x3 = [x[0],x[1] + 1]
    x4 = [x[0],x[1] - 1]
    dic = {}
    L = []
    dic[manhattan(x1)] = x1
    L.append(manhattan(x1))
    dic[manhattan(x2)] = x2
    L.append(manhattan(x2))
    dic[manhattan(x3)] = x3
    L.append(manhattan(x3))
    dic[manhattan(x4)] = x4
    L.append(manhattan(x4))
    
    if(maxma):
        return dic[max(L)]
    else:
        return dic[min(L)]
if(T == 1):
    maxma = True
else:
    maxma = False
x = [0,0]
cnt = 0
for i in S:
    if(i == "U"):
        x[1] += 1
    elif(i == "D"):
        x[1] -= 1
    elif(i == "L"):
        x[0] -= 1
    elif(i == "R"):
        x[0] += 1
    else:
        cnt += 1
for i in range(cnt):
    x = man(x,maxma)
print(manhattan(x))

