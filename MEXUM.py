def mex(a):
    if len(a)==0:
        return 1
    else:
        for i in range(1,max(a)+1):
            if i not in a:
                return i
                break
from itertools import permutations
t = int(input())
for _ in range(t):
    n = int(input())
    sum1 = 
    a = list(map(int,input().split()))
    for k in permutations(a):


