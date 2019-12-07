t = int(input())
for _ in range(t):
    n , m , q = map(int,input().split())
    #a = np.zeros([n,m], dtype=int)
    a = []
    
    for i in range(n):
        matrix = []
        for j in range(m):
            matrix.append(0)
        a.append(matrix)
    op = 0
    for _ in range(q):
        x , y = map(int,input().split())
        for i in range(n):
            a[i][y-1] += 1
        for j in range(m):
            a[x-1][j] += 1
    for i in range(n):
        for j in range(m):
            if(a[i][j]%2 != 0):
                op += 1
    print(op)
    



