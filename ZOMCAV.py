t = int(input())
for _ in range(t):
    n = int(input())
    c = list(map(int,input().split()))
    h = list(map(int,input().split()))
    b = [0]*(n)
    for i in range(1,n):
        if i-c[i-1]>0:
            b[i] += 1
        if i+c[i-1]<=n:
            b[i]+=1
    print(b)
