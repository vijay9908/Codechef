from sys import stdin,stdout
from contextlib import suppress


def  countBits(n): 
    count = 0
    while (n): 
        count += n & 1
        n >>= 1
    return count 
    
t = int(input())
for _ in range(t):
    n , q = stdin.readline().split()
    n = int(n)
    q = int(q)
    a = [int(x) for x in stdin.readline().split()]
    odds , evens = 0 , 0
    for ele in a:
        z = countBits(ele)
        if z%2 == 0:
            evens += 1
        else:
            odds += 1
    for _ in range(q):
        p = int(stdin.readline())
        z = countBits(p)
        evens = str(evens)
        odds = str(odds)
        if z%2 == 0:
            stdout.write(evens + ' ' + odds +'\n')
        else:
            stdout.write(odds + ' ' + evens + '\n')         

