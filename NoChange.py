import math

t = int(input())
for _ in range(t):
    n , p = map(int,input().split())
    a = list(map(int,input().split()))[:n]
    b = a[:] 
    cut = 0
    for i in range(0,n-1):
        if a[i+1]%a[i] != 0:
            cut = 1
            break;
    if cut==0 and p%a[n-1]==0:
        print("NO")
    else:
        print("YES",end = " ")
        flg = 1
        m = 0
        for i in range(n):
            if p%a[i]!=0 and a[i]!=1:
                m = i
                flg = 0
                break;
    if flg==0:
        for i in range(m):
            print("0" , end = " ")
        k = math.ceil(p/a[m]) + 1
        print(k , end = " ")
        for i in range(m+1,n):
            print("0", end = " ")
        print()
    else:
        w = [0]*n
        f = 0
        for i in range(n-1,0,-1):
            if p%a[i]==0 and p>0:
                f = math.ceil(p/a[i])-1
                p -= a[i]*f
            elif z>=0:
                f = math.ceil(p/a[i]) + 1
                p -= a[i]*f
            else:
                f = 0
            for u in range(n):
                if b[u] == a[i]:
                    w[u] = f
                    break;
        print(*w)
    

    
            

