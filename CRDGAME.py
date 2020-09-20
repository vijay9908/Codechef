from collections import defaultdict , deque
from sys import stdin , stdout
import math , heapq
listin = lambda: list(map(int,input().split()))
mapin = lambda: map(int,input().split())

t = int(input())
for _ in range(t):
    n = int(input())
    ac , bc = 0 , 0
    for i in range(n):
        a ,b = mapin()
        a , b = sum(map(int,str(a))) , sum(map(int,str(b)))
        if a>b:
            ac += 1
        elif a<b:
            bc += 1
        else:
            ac += 1 
            bc += 1
    if ac > bc:
        print(0,ac)
    elif bc > ac:
        print(1,bc)
    else:
        print(2,ac)       


