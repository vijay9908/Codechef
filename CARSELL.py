t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    a.sort(reverse=True)
    sum = 0
    for i in range(n):
        q = a[i]-i
        if q>0:
            sum += q
    print(sum%1000000007)