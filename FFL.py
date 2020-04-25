s = int(input())
for _ in range(s):  
    n , k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    mina,minb = 999 , 999
    for i in range(n):
        if b[i] == 1:
            mina = min(mina,a[i])
        if b[i] == 0:
            minb = min(minb,a[i])
    q = k+mina+minb
    if  q <= 100:
        print('yes')
    else:
        print('no')

