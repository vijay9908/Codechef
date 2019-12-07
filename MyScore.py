t = int(input())
for _ in range(t):
    n = int(input())
    a = [0,0,0,0,0,0,0,0]
    for i in range(n):
        p , s = map(int,input().split())
        if(p<=8):
            a[p-1] = max(a[p-1],s)
    print(sum(a)) 
        
