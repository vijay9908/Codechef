
t = int(input())
for _ in range(t):
    n = int(input())
    a = input().replace(' ','')
    q = []
    count = 0
    q.append(a.count('101'))
    q.append(a.count('1001'))
    q.append(a.count('10001'))
    q.append(a.count('100001'))
    q.append(a.count('11'))
    for ele in q:
        if ele>0:
            count += 1
    if count>0:
        print('NO')
    else:
        print('YES')


            
            
            
                

            
