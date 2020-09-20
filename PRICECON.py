from collections import defaultdict , deque
from sys import stdin , stdout
import math , heapq
listin = lambda: list(map(int,input().split()))
mapin = lambda: map(int,input().split())
from collections import deque
from sys import stdin,stdout
from itertools import chain

t = int(input())
for _ in range(t):
    n, k = map(int,input().split())
    a = listin()
    q2 = 0
    for ele in a:
        if ele > k:
            q2 += abs(ele-k)
    print(q2)
    


