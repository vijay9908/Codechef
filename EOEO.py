from collections import defaultdict , deque
from sys import stdin , stdout
import math , heapq
listin = lambda: list(map(int,input().split()))
mapin = lambda: map(int,input().split())

def gamer(n):
    status = True
    if n%2 != 0:
        jerrys = list(range(2,n,2))
        for ele in jerrys:
            if n%2 == 0 and ele%2 == 0:
                n , ele = n//2 , ele//2
            elif n%2 != 0 and ele%2 != 0:
                jerrys.remove(ele)
            elif n%2==0 and ele%2!=0:
                jerrys.remove(ele)
        return len(jerrys)
    else:
        jerrys = list(range(1,n+1,2))
        for ele in jerrys:
            if n%2 == 0 and ele%2 == 0:
                n , ele = n//2 , ele//2
            elif n%2 != 0 and ele%2 != 0:
                jerrys.remove(ele)
            elif n%2==0 and ele%2!=0:
                jerrys.remove(ele)
        return len(jerrys)

t = int(input())
for _ in range(t):
    n = int(input())
    print(gamer(n))
    


    

