T = int(input())
for _ in range(T):
    n , k = map(int,input().split())
    a = list(map(int,input().split()))[:n]
    div = 0
    for ele in a[:-1]:
        div += (ele%k)
    print(((a[n-1]+div)%k))
