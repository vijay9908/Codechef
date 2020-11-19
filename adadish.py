from math import ceil
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    a.sort(reverse=True)
    count = 0
    """ if len(set(a)) == 1:
        count = ceil(n/2)*a[0]
    elif n == 2:
        count += a[0]
    else: """
    v1,v2 = a[0] , a[1]
    for i in range(2,n):
        if v1 < v2:
            v1 += a[i]
        else:
            v2 += a[i]
    count = max(v1,v2)
    print(count)         
    
