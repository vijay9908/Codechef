from collections import deque

vst = deque()
vst.append((1,2,3,4,5,6,7,8,9))
vstd = {(1,2,3,4,5,6,7,8,9):0}

primes = (3,5,7,11,13,17)
changes = [(0,1),(0,3),(1,2),(1,4),(2,5),(3,4),(3,6),(4,5),(4,7),(5,8),(6,7),(7,8)]

count = 0

while(len(vst)>0):
    for _ in range(len(vst)):
        l = list(vst.popleft())
        for n1,n2 in changes:
            if l[n1]+l[n2] in changes:
                l[n1] , l[n2] = l[n2] , l[n1]
                if tuple(l) not in vstd:
                    vst.append(tuple(l))
                    vstd[tuple(l)] = count + 1
                l[n1] , l[n2] = l[n2] , l[n1]
    count += 1

t = int(input())
for i in range(t): 
    a = []
    for _ in range(3):
        a.extend(list(map(int,input().split())))
    k = tuple(a)
    print(vstd[k] if k in vstd else -1)