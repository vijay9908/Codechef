from collections import defaultdict , deque
from sys import stdin , stdout
import math , heapq
listin = lambda: list(map(int,input().split()))
mapin = lambda: map(int,input().split())

def power2(num):
    if (num & (num-1)) == 0:
        return True
    return False

t = int(input())
for _ in range(t):
    n = int(input())
    tom , jerry , power = n , 0 , 0
    while n%2==0:
        power += 1
        n = n//2
    jerry = int(math.pow(2,power+1))
    count = 0
    if jerry<=tom:
        count = tom//jerry
    print(count)
    
