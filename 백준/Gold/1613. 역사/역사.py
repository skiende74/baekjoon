import sys
input = sys.stdin.readline
V, E = map(int,input().split())
grid = [[0]*(V+1) for _ in range(V+1)]
for _ in range(E):
    i, j= map(int,input().split())
    grid[i][j] = 1

for k in range(1,V+1):
    for i in range(1,V+1):
        for j in range(1,V+1):
            if grid[i][k] and grid[k][j]:
                grid[i][j] = 1

Q = int(input())
for _ in range(Q):
    i,j = map(int,input().split())
    if grid[i][j]:
        print(-1)
    elif grid[j][i]:
        print(1)
    else:
        print(0)
