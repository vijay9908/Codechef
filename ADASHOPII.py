from collections import deque
from sys import stdin,stdout
from collections import defaultdict 
from itertools import chain

def is_safe(k,k1):
    if(k>0 and k1>0 and k<9 and k1<9):
        v.append((k,k1))

t = int(input())
for  _ in range(t):
    r , c = map(int,input().split())
    moves = [(2,2),(1,3),(3,1),(2,2),(3,3),(2,4),(1,5),(4,2),(5,1),(3,3),(4,4),(3,5),(2,6),(1,7),(5,3),(6,2),(7,1),(4,4),(5,5),(4,6),(3,7),(2,8),
            (6,4),(7,3),(8,2),(5,5),(6,6),(5,7),(4,8),(7,5),(8,4),(6,6),(7,7),(6,8),(8,6),(7,7),(8,8),(8,8)]
    q = (r+c)//2
    k = len(moves)
    k += 2
    print(k)
    print(q,q)
    print(1,1)
    for item in moves:
        n1,n2 = item
        print(n1,n2)

t = int(stdin.readline())
for _ in range(t):
    r , c = stdin.readline().split()
    r , c = int(r),int(c)
    v = deque()
    q = (r+c)//2
    v.append((q,q))
    v.append((1,1))
    for i in range(2,9):
        v.append((i,i))
        k , k1 = i ,i 
        for j in range(i-1,0,-1):
            k -= 1
            k1 += 1
        is_safe(k,k1)
        k , k1 = i , i
        for j in range(i+1,9):
            k += 1
            k1 -= 1
            is_safe(k,k1)
        v.append((i,i))
    print(len(v))
    for item in v:
        n1,n2 = item
        print(n1,n2)
    """ for item in v:
        print(item) """



