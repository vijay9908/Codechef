from sys import stdin,stdout

a , b = stdin.readline().split()
a , b = int(a) , int(b)
count = 0
for i in range(a):
    ino = int(stdin.readline())
    if ino%b == 0:
        count+=1
print(count)