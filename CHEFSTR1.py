from collections import defaultdict , deque
from sys import stdin , stdout
import math , heapq
listin = lambda: list(map(int,input().split()))
mapin = lambda: map(int,input().split())

t= int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))[:n]
    count = 0
    for i in range(n-1):
        count += (abs(a[i+1]-a[i])-1)
    print(count)