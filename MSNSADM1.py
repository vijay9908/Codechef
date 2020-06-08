from collections import defaultdict,deque
from itertools import permutations , combinations
from sys import stdin , stdout

t = int(input())
for _ in  range(t):
    n = int(input())
    a = list(map(int,input().split()))[:n]
    b = list(map(int,input().split()))[:n]
    for i in range(n):
        a[i] = 20*a[i] - 10*b[i]
    if max(a)>0:
        print(max(a))
    else:
        print(0)
