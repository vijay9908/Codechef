from collections import defaultdict,deque

def compute(k,i,j,sheets): 
    return (k+1) - abs(i-j) - sheets
    
def sheet_compute(s,i,j):
    y = 0
    for q in range(i,j+1):
        if s[q] == ':':
            y += 1
    return y

for _ in range(int(input())):
    n , k = map(int,input().split())
    s = input()
    i, j = 0, 0
    count, res = 0, 0
    sheets = 0
    while i<n and j<n:
        if s[i] == 'M':
            if s[j] == 'I':
                sheets = sheet_compute(s,min(i,j),max(j,i))
                res = compute(k,i,j,sheets)
                if res>0:
                    count += 1
                    i += 1
                    j += 1
                elif i > j:
                    j += 1
                else:
                    i += 1
            elif s[j] == 'X':
                i = j
                i += 1
                j += 1
            else:
                j += 1
        elif s[i] == 'X':
            j = i
            i += 1
            j += 1
        else:
            i += 1
    print(count)