from collections import defaultdict


t = int(input())
for _ in range(t):
    n , q = map(int,input().split())
    s = list(input().strip())
    k = defaultdict(int)
    for i in range(n):
        k[s[i]] += 1
    for i in range(q):
        count = 0
        w = int(input())
        for items in k.values():
            if items > w:
                count += abs(items-w)
        print(count)
        count = 0


