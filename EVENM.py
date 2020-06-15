from collections import defaultdict , deque
from sys import stdin , stdout
from math import gcd
import heapq
listin = lambda: list(map(int,input().split()))
mapin = lambda: map(int,input().split())
from itertools import permutations
from functools import reduce 
from operator import mul

""" def reshape(lst, shape):
    if len(shape) == 1:
        return lst
    n = reduce(mul, shape[1:])
    return [reshape(lst[i*n:(i+1)*n], shape[1:]) for i in range(len(lst)//n)]

t = int(input())
for _ in range(t):
    n = int(input())
    for p in permutations(range(1,n**2+1)):
        status , status2 = True,False
        for i in range(1,n**2+1):
            if i+n+1 <= n**2:
                if (p[i]+p[i+n]+1)%2==0 and (p[i]+p[i+n-1])%2==0:
                    status = True
                else:
                    status = False
        if status:
            print(reshape(p, [n]*n))
            status2 = True
            break
        if status2:
            break """

t = int(input())
for _ in range(t):
    n = int(input())
    ele = 1
    for i in range(n):
        if i%2 == 0:
            for j in range(n):
                print(ele,end=' ')
                ele += 1
        else:
            ele = ele+n-1
            for j in range(n):
                print(ele,end=' ')
                ele -= 1
            ele = ele+n+1
        print()
