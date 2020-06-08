from collections import defaultdict , deque
from sys import stdin , stdout
import math , heapq
listin = lambda: list(map(int,input().split()))
mapin = lambda: map(int,input().split())

def func(a,n):
    q = [0,0,0]
    status = True
    if a[0] != 5:
        return False
    else:
        q[0] += 1
        for i in range(n):
            if a[i]-5 == 5:
                if q[0] > 0:
                    q[0] -= 1
                    q[1] += 1
                else:
                    status = False
            elif a[i]-5 == 10:
                if q[1] > 0:
                    q[1] -= 1
                    q[2] += 1
                else:
                    status = False
    return status

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))[:n]
    print('YES') if func(a,n) else print('NO')
    
    

    
