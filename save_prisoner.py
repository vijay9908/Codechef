t = int(input())
for _ in range(t):
    n , m , s = map(int,input().split())
    k = (n+m+s-1)%n
    if(k==0):
        print(n)
    else:
        print(k)