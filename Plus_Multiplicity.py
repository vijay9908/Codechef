import math 
t = int(input())

def fact(n):  
    if (n <= 1): 
        return 1 
    return n * fact(n - 1)  
def nPr(n, r):  
    return math.floor(fact(n) / fact(n - r))

for _ in range(t):
    n = int(input())
    count = 0
    a = list(map(int,input().split()))
    twos = a.count(2)
    zeros = a.count(0)
    print((twos*(twos-1))//2 + (zeros*(zeros-1))//2)
    
             
        