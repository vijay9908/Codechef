
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))[:n]
    b = list(map(int,input().split()))[:n]
    sum = 0
    for (ele1,ele2) in zip(sorted(a),sorted(b)):
        sum += min(ele1,ele2)
    print(sum)
        

            


