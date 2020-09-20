from collections import defaultdict , deque
from sys import stdin , stdout
import math , heapq
listin = lambda: list(map(int,input().split()))
mapin = lambda: map(int,input().split())

def or_done(a,n):
    k = a[0]
    count = 1
    for i in range(n):
        if (k | a[i]) > k :
            k = k|a[i]
            count += 1
    return count

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    print(or_done(a,n))