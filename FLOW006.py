t = int(input())
for _ in range(t):
    a = input()
    sum = 0
    while(a != ''):
        sum += int(a[-1])
        a = a[:-1]
    print(sum)
