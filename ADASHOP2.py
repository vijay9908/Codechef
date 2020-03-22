from collections import defaultdict
from sys import stdin,stdout
from collections import deque
from itertools import chain

def issafe(x,y):
    return (x>=0 and x<=7 and y>=0 and y<= 7)
def rem_dups(p): 
    return list(set([i for i in p])) 

t = int(stdin.readline())
for _ in range(t):
    moves = 0
    list = []
    r0 , c0 = map(int,input().split())
    count = 0
    x , y = [-1,-1,1,1,] , [-1,1,-1,1]
    xq , yq = deque() , deque()
    xq.append(r0)
    yq.append(c0)
    while(len(xq)>0):
        count += 1
        xx = xq.popleft()
        yy = yq.popleft()
        if count >= 64:
            break
        pair = (xx,yy)
        list.append(pair)
        moves += 1

        for i in range(4):
            xx += x[i]
            yy += y[i]
            if issafe(xx,yy):
                xq.append(xx)
                yq.append(yy)
print(moves)
list = set([i for i in list])
for item in list:
    n1,n2 = item
    print(n1,n2)

    moves = [(2,2),(1,3),(3,1),(2,2),(3,3),(1,5),(2,4),(5,1),(4,2),(3,3),(4,4),(1,7),(2,6),(3,5),(7,1),(6,2),(5,3),(4,4),(5,5),(2,8),(3,7),(4,6),(6,4),(7,3),(8,2),(5,5),(6,6),(4,8),(5,7),(7,5),(8,4),(6,6),(7,7),(6,8),(8,6),(7,7),(8,8)]
    for items in moves:
        if((r,c) == item):
            moves.remove((r,c))
    print(len(moves))    

    
    
