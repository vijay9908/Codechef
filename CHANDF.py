def get_prod(a,b,c):
    return (a&b)*(a&c)

t = int(input())
for _ in range(t):
    a , b , l , r = map(int,input().split())
    print(a|b)
    
    