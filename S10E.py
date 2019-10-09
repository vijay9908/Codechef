try:
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int,input().split()))[:n]
        count = 0
        for i in range(n):
            k = 0
            for j in range(i-5,i):
                if(a[i] >= a[j] and j >= 0):
                    k = 1
                    break
            if(k == 0):                
                count += 1
        print(count)
except:
    pass

    
 

            

        
    

