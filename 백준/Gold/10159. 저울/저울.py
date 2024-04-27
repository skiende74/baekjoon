import sys
input = sys.stdin.readline
V = int(input())
E = int(input())
grid = [[0]*(V+1) for _ in range(V+1)]
for i in range(1,V+1): grid[i][i] = 1
for _ in range(E):
    i, j = map(int,input().split())
    grid[i][j] = 1
    grid[j][i] = -1

for k in range(1,V+1):
    for i in range(1,V+1):
        for j in range(1,V+1):
            if grid[i][k]==1 and grid[k][j]==1:
                grid[i][j]=1
            if grid[i][k]==-1 and grid[k][j]==-1:
                grid[i][j]=-1

for i in range(1,V+1):
    g = grid[i][1:]
    print(V-g.count(1)-g.count(-1))
