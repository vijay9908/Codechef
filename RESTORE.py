def func(n):
    a = [1]
    prime = [True for i in range(n+1)]
    p = 2
    while p*p <= n:
        if prime[p] == True:
            for i in range(p*p,n+1,p):
                prime[i] = False
        p += 1
    for p in range(2,n+1):
        if prime[p]:
            a.append(p)
    return a

c = func(4*10**6)
for _ in range(int(input())):
    n = int(input())
    b = list(map(int,input().split()))
    a = c[:n+1]
    i = 0
    temp = [0 for _ in range(n)]
    while i < n:
        if (i+1) != b[i]:
            temp[i] = a[b[i]]
        elif i+1 == b[i]:
            temp[i] = a[b[i]]
        i += 1
    print(*temp)

    
