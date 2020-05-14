N,K = map(int,input().split())
L = []
for i in range(K):
    d = int(input())
    A = list(map(int,input().split()))
    for j in A:
        L.append(j)
        
print(N-len(set(L)))
