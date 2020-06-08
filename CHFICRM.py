from collections import defaultdict , deque
from sys import stdin , stdout
import math , heapq
listin = lambda: list(map(int,input().split()))
mapin = lambda: map(int,input().split())

def func(a):
    coll = []
    status = False
    if a[0] == 5:
        coll.append(5)
        status = True
    else:
        return False
    for i in range(1,n):
        if a[i]-5 in coll:
            coll.remove(a[i]-5)
            coll.append(a[i])
            status = True
        elif ((a[i]-5)//2 in coll) and (coll.count((a[i]-5)//2) >= 2):
            coll.remove((a[i]-5)//2)
            coll.remove((a[i]-5)//2)
            status = True
        elif a[i] == 5:
            coll.append(5)
            status = True
        else:
            status = False
            break
    return status

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))[:n]
    print('YES') if func(a) else print('NO')



    

