from collections import defaultdict , deque
from sys import stdin , stdout
import math , heapq
listin = lambda: list(map(int,input().split()))
mapin = lambda: map(int,input().split())

t = int(input())
for _ in range(t):
    p , q , r = map(int,input().split())
    a , b , c = map(int,input().split())
    d = defaultdict(int)
    d2 = defaultdict(int)
    if p-a != 0:
        d[abs(p-a)] += 1
        
    if q-b != 0:
        d[abs(q-b)] += 1 
    if r-c != 0:
        d[abs(r-c)] += 1
    print(d.items())