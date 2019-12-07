import math 
t = int(input())
for _ in range(t):
    n = int(input())
    count = 0
    a = list(map(int,input().split()))
    def fact(n):  
        if (n <= 1): 
            return 1 
        return n * fact(n - 1)  
    def nPr(n, r):  
        return math.floor(fact(n) / fact(n - r))
    twos = a.count(2)
    zeros = a.count(0)
    if(twos >= 1 and twos < n):
        print(nPr(twos,2)//2)
    else:
        print(nPr(twos,2))
             
        