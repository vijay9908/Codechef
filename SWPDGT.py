from itertools import permutations

t = int(input())
for _ in range(t):
    a , b = map(str,input().split())
    a = list(a.strip())
    b = list(b.strip())
    max_sum = 0
    for ele in a:
        for ele2 in b:
            ele , ele2 = int(ele) , int(ele2)
        
