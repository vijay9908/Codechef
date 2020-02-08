T = int(input())
g_sum = 0
for _ in range(T):
    n = int(input())
    q = [[0 for i in range(4)] for j in range(4)]
    for _ in range(n):
        m , k =  input().split()
        k = int(k)
        w = 0
        if(m =='A'):
            w = 0
        elif(m =='B'):
            w = 1
        elif(m =='C'):
            w = 2
        else:
            w = 3
        q[w][(k//3)-1] += 1
        w = 0
    e = []
    for i in range(4):
        e.append(max(q[i]))
    e.sort(reverse=True)
    sum = 0
    h = 100
    for ele in e:
        if ele==0:
            sum -= 100
        else:
            sum += (ele*h)
            h -= 25
    g_sum += sum
    print(sum)
print(g_sum)



        

        




        
                

