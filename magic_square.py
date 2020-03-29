from itertools import permutations

a = []
for _ in range(3):
    a.extend(list(map(int,input().split())))
count = 100
for p in permutations(range(1,10)):
    if( sum(p[0:3])==15 and sum(p[3:6])==15 and sum(p[0::3])==15 and sum(p[1::3])==15 and (p[0]+p[4]+p[8]==15) and (p[2]+p[4]+p[6]==15) ):
        count = min(count,sum(abs(p[i]-a[i]) for i in range(9)))
print(count)