d = [[0 for i in range(1,n)] for j in range(1,n)]
for k in range(1,n):
    for i in range(1,n):
        for j in range(1,n):
            d[i][j] - min(d[i][j],d[i][k]+d[k][j])

shortest = 999999999
for item in itertools.permutations(d):
    shortest = min(shortest,d)
    # d being d[0][1] + d[start][a[1]] + d[a[1]a[2]].....
