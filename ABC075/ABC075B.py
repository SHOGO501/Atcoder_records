#!/usr/bin/env python
# coding: utf-8

# In[35]:


import itertools
H,W = map(int,input().split())
grid = []
for i in range(H):
    a = input()
    l = []
    for i in a:
        if(i == "."):
            i = 0
        l.append(i)
    grid.append(l)
for i in range(H):
    for j in range(W):
        if(grid[i][j] != "#"):
            continue
        for dx,dy in itertools.product([-1,0,1],repeat=2):
            x = i + dx
            y = j + dy
            if(x<0 or H<=x):
                continue
            if(y<0 or W <= y):
                continue
            if grid[x][y] == "#":
                continue
            grid[x][y] += 1
for Row in grid:
    print(*Row,sep="")


# In[ ]:




