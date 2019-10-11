t = int(input())
for _ in range(t):
    n , k = map(int,input().split())
    a = list(map(int,input().split()))[:n]
    if(k<=3*n):
        for i in range(k):
            b = a[i%n]
            c = a[n-(i%n)-1]
            a[i%n] = b^c
        for i in range(n):
            print(a[i],end=' ') 
    else:
        k %= (3*n)   
        for i in range(k):
            b = a[i%n]
            c = a[n-(i%n)-1]
            a[i%n] = b^c
        if(n%2 != 0):
            a[n//2] = 0
        for i in range(n):
            print(a[i],end=' ')
    print()