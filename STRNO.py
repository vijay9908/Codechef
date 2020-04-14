from sys import stdin , stdout
import math

def factors(a,b):
    facts = []
    while(a%2==0):
        facts.append(2)
        a/=2
    for i in range(3,int(math.sqrt(a)),2):
        if a > i*i:
            while a%i == 0:
                a /= i
                facts.append(i)
    if a>2:
        facts.append(a)
    if len(facts)<b:
        return 0
    else:
        return 1

t = int(input())
for _ in range(t):
    a , b = map(int,input().split())
    print(factors(a,b))