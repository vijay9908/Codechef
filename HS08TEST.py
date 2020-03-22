from collections import defaultdict
from sys import stdin , stdout

x , y = map(float,input().split())
if(x%5 == 0 and (x+0.50 <= y)):
    y-=x
    y-=0.50
print(y)
