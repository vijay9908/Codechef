def f(i, a, b):
    if (a == 0 and b == 0):
        return 1

    elif ((n - i) == a and (n - i) == b):
        return 1

    elif (n - i) == a:
        return 2 * (f(i+1, a-1, b-1) + f(i+1, a-1, b))

    elif (n - i) == b:
        return 2 * (f(i+1, a-1, b-1) + f(i+1, a, b-1))
    
    return 2 * (f(i+1, a-1, b-1) + f(i+1, a-1, b) + f(i+1, a, b-1) + f(i+1, a, b))

  

t = int(input())
for _ in range(t):
    n = int(input())
    a = str(input())
    b = str(input())
    a = a.count('1')
    b = b.count('1')
    k = f(0,a,b)
    print(k)

  