from collections import deque
from sys import stdin,stdout
from itertools import chain

class Point: 
	def __init__(self, x, y): 
		self.x = x 
		self.y = y 

def onSegment(p, q, r): 
	if ( (q.x <= max(p.x, r.x)) and (q.x >= min(p.x, r.x)) and
		(q.y <= max(p.y, r.y)) and (q.y >= min(p.y, r.y))): 
		return True
	return False

def orientation(p, q, r): 
	val = (float(q.y - p.y) * (r.x - q.x)) - (float(q.x - p.x) * (r.y - q.y)) 
	if (val > 0): 
		return 1
	elif (val < 0):  
		return 2
	else: 
		return 0

def doIntersect(p1,q1,p2,q2): 
	o1 = orientation(p1, q1, p2) 
	o2 = orientation(p1, q1, q2) 
	o3 = orientation(p2, q2, p1) 
	o4 = orientation(p2, q2, q1) 
 
	if ((o1 != o2) and (o3 != o4)): 
		return True

	if ((o1 == 0) and onSegment(p1, p2, q1)): 
		return True

	if ((o2 == 0) and onSegment(p1, q2, q1)): 
		return True

	if ((o3 == 0) and onSegment(p2, p1, q2)): 
		return True

	if ((o4 == 0) and onSegment(p2, q1, q2)): 
		return True

	return False

t = int(stdin.readline())
for _ in range(t):
    n , q = map(int,input().split())
    a = list(map(int,input().split()))[:n]
    points = []
    for i,item in enumerate(a):
        points.append((i+1,item))
    for _ in range(q):
        intersects = 0
        x1 , x2 , y = stdin.readline().split()
        x1 , x2 , y = int(x1) , int(x2) , int(y)
        p2 = Point(x1,y)
        q2 = Point(x2,y)
        for j in range(n-1):
            l11 , l12 = points[j]
            l21 , l22 = points[j+1]
            if ((l11==x2 and l12==y) or (l21==x1 and l22==y)):
                continue
            p1 = Point(l11,l12)
            q1 = Point(l21,l22)
            if(doIntersect(p1,q1,p2,q2)):
                intersects += 1
        print(intersects)
        

        
    


