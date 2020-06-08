from collections import defaultdict,deque
from itertools import permutations , combinations
from sys import stdin , stdout

t = int(input())
for _ in range(t):
    n , k =map(int,input().split())
    print('NO') if n%(k*k)==0 else print('YES')
        