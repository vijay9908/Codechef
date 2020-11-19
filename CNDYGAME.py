t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    k = int(input())
    for q in range(k):
        p  = int(input())
        chef, chefy = 0 , 0
        index = 0
        control = False
        while index < p:
            #if index!=0 and index%n==0:
             #   chef,chefy = chefy,chef
            i = index
            if i < n and index < n:
                if a[i] == 1:
                    if i==0 and i+1<n and index<p:
                        chef += a[i]
                        chef,chefy = chefy, chef
                        i += 1
                        index += 1
                        chef += a[i] if a[i]%2!=0 else a[i]-1
                        chef, chefy = chefy, chef
                    elif i == n-1:
                        chef += a[i]
                        chef,chefy = chefy,chef
                    elif i!=0 and i+1<n-1 and index<p:
                        chef += a[i]
                        chef, chefy = chefy, chef
                        i += 1
                        index += 1
                        chef += a[i] if a[i]%2!=0 else a[i]-1
                        chef,chefy = chefy, chef
                else:
                    chef += a[i] if a[i]%2==0 else a[i]-1
            else:
                i = index%n
                if i == 0:
                    chef,chefy = chefy,chef
                if i < n and index < p:
                    if a[i] == 1:
                        if i==0 and i+1<n and index<p:
                            chef += a[i]
                            chef,chefy = chefy, chef
                            i += 1
                            index += 1
                            chef += a[i] if a[i]%2!=0 else a[i]-1
                            chef, chefy = chefy, chef
                        elif i == n-1:
                            chefy += a[i]
                            chef, chefy = chefy, chef
                        elif i!=0 and i+1<n-1 and index<p:
                            chef += a[i]
                            chef, chefy = chefy, chef
                            i += 1
                            index += 1
                            chef += a[i] if a[i]%2!=0 else a[i]-1
                            chef,chefy = chefy, chef
                    else:
                        chef += a[i] if a[i]%2==0 else a[i]-1
            index += 1
            
        print(chef%(10**9+7))
        #print("----",chef,chefy)


                

            
            
            

                
            
            