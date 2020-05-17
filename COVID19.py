t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    count = 0
    low_arr = []
    for i in range(n-1):
        if a[i+1]-a[i] <= 2:
            count += 1
        else:
            low_arr.append(count+1)
            count = 0
    low_arr.append(count+1)
    
    print(min(low_arr),max(low_arr))