from collections import defaultdict,deque
from itertools import permutations

t = int(input())
for _ in range(t):
    n = int(input())
    if n==1:
        print(1)
    else:
        print(n//2)
    if n==1:
        print ('%d   %d' % (1,1))
        continue
    elif n==2:
        print ('%d %d %d' % (1,1,2))
        continue
    elif n==3:
        print ('%d %d %d %d' % (1,1,2,3))
        continue
    else:
        if n%2 != 0:
            print ('%d %d %d %d' % (3,1,2,n))
        else:
            print ('%d %d %d' % (2,1,2))
        if n%2 != 0:
            n -= 1
        for i in range(3,n,2):
            print ('%d %d %d' % (2,i,i+1))
