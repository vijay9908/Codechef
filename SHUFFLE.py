t = int(input())
for _ in range(t):
    n , k = map(int,input().split())
    a = list(map(int,input().split()))
    for i in range(n):
        for j in range(k,n):
            if a[j-k]>-1 and a[j-k] > a[j]:
                temp = a[j-k]
                a[j-k] = a[j]
                a[j] = temp
    if a == sorted(a):
        print('yes')
    else:
        print('no')