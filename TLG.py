t = int(input())
sum1 , sum2  = 0 , 0 
lead=[1,0]
for _ in range(t):
    a , b = map(int,input().split())
    sum1 += a
    sum2 += b
    if sum1 > sum2:
        sum = sum1 - sum2
        if sum > lead[1]:
            lead[0] = 1
            lead[1] = sum
    else:
        sum = sum2 - sum1
        if sum > lead[1]:
            lead[0] = 2
            lead[1] = sum
print("{} {}".format(lead[0],lead[1]))
        
        
    