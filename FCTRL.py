def fact(n):
    if n == 1:
        return n
    return n*fact(n-1)

t = int(input())
for _ in range(t):
    n = int(input())
    print(fact(n))