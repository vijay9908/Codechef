from collections import defaultdict

t  = int(input())
for _ in range(t):
    y , z = map(int,input().split())
    m = defaultdict(int)
    c = list(map(int,input().split()))
    a = [0]
    b = [0]*(y+1)
    for i in range(1,y+1):
        a.append(c[i-1])
        m[a[i]] = i
        if a[i] == i:
            b[i]=1
    v , v1 , v2 , v3 = [] , [] , [] , []
    k , k1, k2 , k3 = 0, 0, 0, 0
    for i in range(1,y+1):
        if a[i]!=i and b[i]==0:
            k , k1 , k2, k3 = i , m[i] , a[i] , m[m[i]]
        if m[i]!=a[i]:
            v1.append(k3)
            v2.append(k1)
            v3.append(k)
            a[i] = k
            a[k1] = k1
            a[k3] = k2
            m[i] = k
            m[k1] = k1
            m[k2] = k3
        else:
            v.append(i)
            v.append(a[i])
            b[i] = 1
            b[a[i]] = 1
    if len(v)%4==0:
        for j in range(0,len(v)):
            v1.append(v[j])
            v2.append(v[j+1])
            v3.append(v[j+2])
            v1.append(v[j+3])
            v2.append(v[j+2])
            v3.append(v[j])
    print(len(v1),len(v))
    if len(v1)>z or len(v)%4!=0:
        print(-1)
    else:
        print(len(v1))
        for i in range(len(v1)):
            print(v1[i],v2[i],v3[i])