import math
def fact(n):
    if(n <= 1):
        return 1
    return n * fact(n - 1)

def nPr(n,r):
    return math.floor(fact(n)/fact(n-r))

def Adata(a):
    return a.count('0') , a.count('1')

def digits(a):
    k0 = a.count('0')
    k1 = a.count('1')
    if(k0 >= 1 and k1 >= 1):
        return 2
    else:
        return 1

t = int(input())
for _ in range(t):
    n = int(input())
    a = str(input())
    b = str(input())
    a_data = [a.count('0'),a.count('1')]
    b_data = [b.count('0'),b.count('1')]
    q = nPr(n,digits(a))//fact(digits(a))
    w = nPr(n,digits(b))//fact(digits(b))
    print(w*q)
