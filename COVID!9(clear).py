t = int(input())
for _ in range(t):
    n = int(input())
    if n==0:
        print(0,0)
    else:
        a = list(map(int,input().split()))
        w = []
        mini = []
        maxi, counter =  0 , 0
        for i in range(n-1):
            if abs(a[i+1]-a[i]) <= 2:
                counter += 1
                maxi = counter

            else:
                counter = 0
        w.append(maxi+1)
        counter = 0
        for i in range(n-1):
            if abs(a[i+1]-a[i]) <= 2:
                counter += 1
            else:
                mini.append(counter)
                counter = 0
        if len(mini)==0:
            w.append(maxi+1)
        else:
            z = min(mini)
            w.append(z+1)
        if w[1]>w[0]:
            print(w[0],w[1])
        else:
            print(w[1],w[0])