from collections import defaultdict

t = int(input())
while t:
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    d = defaultdict(int)
    for i in range(n):
        d[a[i]]+=b[i]
    print(min(d.values()))
    t-=1