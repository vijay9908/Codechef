
t = int(input())
for _ in range(t):
    n , k = map(int,input().split())
    a = list(map(int,input().split()))
    count = 0
    for ele in a:
        if ele<=0:
            count += 1
    if count >= k:
        print('NO')
    else:
        print('YES')