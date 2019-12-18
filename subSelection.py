from collections import Counter as counter 

t = int(input())
for _ in range(t):
    n = int(input())
    s = str(input())
    ma = 0
    for i in range(n):
        m = counter(s[i])+1
        if(m[s[i]]>1):
            m1 = counter(s[i]+1)
            ma = min(ma,(i-m1[s[i]])+1)
            m1[s[i]] = i 
        else:
            m1[s[i]] = i

    if(ma == 0):
        print(0)
    else:
        print(len(s)-ma+1)  
    m.clear()
    m1.clear()

    
            
   
 