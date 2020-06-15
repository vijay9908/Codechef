from collections import defaultdict , deque
from sys import stdin , stdout
import math , heapq
listin = lambda: list(map(int,input().split()))
mapin = lambda: map(int,input().split())

t = int(input())
for _ in range(t):
    n , p = map(int,input().split())
    a = [[1 for j in range(n)] for i in range(n)]
    