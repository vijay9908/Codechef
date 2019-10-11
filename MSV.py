try:
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int,input().split()))
        q = 0
        for i in range(n):
            count = 0
            for j in range(i):
                if(a[j]%a[i] == 0):
                    count += 1
            q = max(count,q)
        print(q)  
except:
    pass    