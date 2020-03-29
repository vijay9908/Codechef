n = int(input())
for _ in range(n):
    x , y , z = map(int,input().split())
    a = abs(z-x)
    b = abs(z-y)
    if a<b:
        print("Cat A")
    elif(a>b):
        print('Cat B')
    else:
        print('Mouse C')