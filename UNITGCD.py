from collections import deque , defaultdict


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def coprime(a, b):
    return gcd(a, b)

def check(list,a):
    kas = True
    for ele in list:
        if coprime(ele,a):
            pass
        else:
            kas = False
            break
    return kas


t = int(input())
for _ in range(t):
    n = int(input())
    a1,a2 = [1] , []
    for i in range(2,n+1):
        ''' print(check(a1,i)) '''
        if check(a1,i):
            a1.append(i)
        else:
            a2.append(i)


print(a1)
print(a2)

            

