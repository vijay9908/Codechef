from collections import defaultdict , deque
from sys import stdin , stdout
import math , heapq
listin = lambda: list(map(int,input().split()))
mapin = lambda: map(int,input().split())

t = int(input())
for _ in range(t):
    n = int(input())
    if n%2 !=0 :
        print(n//2)
    else:
        count = 0
        while(n%2==0):
            n  = n//2
            count += 1
        print(count//2)