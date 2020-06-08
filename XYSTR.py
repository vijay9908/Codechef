from collections import defaultdict , deque
from sys import stdin , stdout
import math , heapq
listin = lambda: list(map(int,input().split()))
mapin = lambda: map(int,input().split())

t = int(input())
for _ in range(t):
    s = list(input().strip())
    cou = 0
    for i in range(len(s)-1):
        if s[i]=='x' and s[i+1]=='y':
            cou += 1
            s[i] , s[i+1] = '0' , '0'
        elif s[i]=='y' and s[i+1]=='x':
            cou += 1
            s[i] , s[i+1] = '0' , '0'
    print(cou)
