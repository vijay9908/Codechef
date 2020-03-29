from collections import Counter

n = int(input())
a = list(map(int,input().split()))
k = Counter(a)

count = 0
for i in range(99):
    count  = max(k[i]+k[i+1],count)
print(count)