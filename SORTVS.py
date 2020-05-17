from collections import defaultdict


t = int(input())
for _ in range(t):
    y , z = map(int,input().split())
    a = list(map(int,input().split()))
    for i in range(y):
        a[i] -= 1
    
    for _ in range(z):
        b = input()
    res = 0
    for i in range(y):
        if a[i] != i:
            k = 0
            for j in range(y):
                if a[j]==i:
                    k = j
            a[i] , a[k] = a[k] , a[i]
            res += 1
    print(res)
    