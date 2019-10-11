import numpy as np

t = int(input())
for _ in range(t):
    n , m , q = map(int,input().split())
    a = np.zeros([n,m], dtype=int)
    op = 0
    for _ in range(q):
        x , y = map(int,input().split())
        for i,j in zip(range(n),range(m)):
            a[i,y-1] += 1
            a[x-1,j] += 1
    for i in range(n):
        for j in range(m):
            if(a[i,j]%2 != 0):
                op += 1
    print(op)