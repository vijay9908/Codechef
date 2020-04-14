t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    count , p1 , p2 = 0 , -1 , -1
    for i in range(n):
        if a[i]%4==0:
            p1 , p2 = i , i
            count += (i+1)
        elif a[i]%2 != 0:
            if p1==-1 and p2==-1:
                count += i+1
            elif p2 == -1:
                count += (i-p1)
            else:
                count += (p2+1+(i-p1))
        elif a[i]%2 == 0:
            if p1 != -1:
                p2 , p1 = p1 , i
            else:
                p1 = i
            if p2 == -1:
                continue
            else:
                count += p2+1
    print(count)
            
        
