import sys
input=sys.stdin.readline

V, E = int(input()), int(input())
INF = 10**9
grid = [[INF]*(V+1) for _ in range(V+1)]
path = [[[i] for i in range(V+1)] for _ in range(V+1)]
for i in range(1,V+1): grid[i][i] = 0
for _ in range(E):
    i,j,w = map(int,input().split())
    grid[i][j] = min(grid[i][j], w)

for k in range(1,V+1):
    for i in range(1,V+1):
        for j in range(1,V+1):
            if grid[i][j] <= grid[i][k]+grid[k][j]: continue
            grid[i][j] = grid[i][k] + grid[k][j]
            path[i][j] = path[i][k] + path[k][j]

def show(i,j):
    return grid[i][j] if grid[i][j] <INF else 0
for i in range(1,V+1):
    for j in range(1, V+1):
        print(show(i,j), end=' ')
    print()

for i in range(1,V+1):
    for j in range(1,V+1):
        if grid[i][j]==INF or i==j:
            print(0)
            continue
        print(len(path[i][j])+1 ,i, *path[i][j])