
# coding: utf-8

# In[49]:


A = input()
B = input()
C = input()
count_A = len(A)-1
count_B = len(B)
count_C = len(C)
card = A[0]
A = A[1:]
while(True):
    if(card == "a"):
        count_A -= 1
        if(count_A == -1):
            print("A")
            break
        card = A[0]
        A = A[1:]
    if(card == "b"):
        count_B -= 1
        if(count_B == -1):
            print("B")
            break
        card = B[0]
        B = B[1:]
    if(card == "c"):
        count_C -= 1
        if(count_C == -1):
            print("C")
            break
        card = C[0]
        C = C[1:]       

