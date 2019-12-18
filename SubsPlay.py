def add(a,b):
    count = 0
    while(b>0):
        u = a^b
        v = a & b
        a = u
        b = v*2
        count += 1
    return count

def bTod(binary):   
    binary1 = binary 
    decimal, i, n = 0, 0, 0
    while(binary != 0): 
        dec = binary % 10
        decimal = decimal + dec * pow(2, i) 
        binary = binary//10
        i += 1
    return decimal  
    
t = int(input())
for _ in range(t):
    a = int(input())
    b = int(input())
    print(add(bTod(a),bTod(b)))
