#!/usr/bin/env python
# coding: utf-8

# In[2]:


import sys
read = sys.stdin.buffer.read#全部読み込むやつ
readline = sys.stdin.buffer.readline#1行読み込むやつ
readlines = sys.stdin.buffer.readlines#リストで読み込むらしい


# In[31]:


from math import factorial
N, A, B = map(int, input().split())
MOD = 10 ** 9 + 7

def calc(n):
    ret = 1
    for i in range(n):
        ret = ret * (N - i) % MOD
    return ret * pow(factorial(n), MOD - 2, MOD) % MOD

print(max(0, (pow(2, N, MOD) - ((calc(A) + calc(B)) % MOD) - 1) % MOD))


# In[ ]:


#maspy ans

from functools import reduce

# %%
stdin = open(0)

# %%
N, A, B = map(int, stdin.read().split())
MOD = 10 ** 9 + 7

# %%


def f(A):
    num = reduce(lambda x, y: x * y % MOD, range(N, N - A, -1))
    den = reduce(lambda x, y: x * y % MOD, range(1, A + 1))
    return num * pow(den, MOD - 2, MOD) % MOD


# %%
answer = pow(2, N, MOD) - f(A) - f(B) - 1
answer %= MOD
print(answer)


# In[ ]:




