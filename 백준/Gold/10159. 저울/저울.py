import sys
input = sys.stdin.readline
V = int(input())
E = int(input())
grid = [[0]*(V+1) for _ in range(V+1)]
for i in range(1,V+1): grid[i][i] = 1
for _ in range(E):
    i, j = map(int,input().split())
    grid[i][j] = 1

for k in range(1,V+1):
    for i in range(1,V+1):
        for j in range(1,V+1):
            if grid[i][k] and grid[k][j]:
                grid[i][j]=1

for i in range(1,V+1):
    count=0
    for j in range(1,V+1):
        if not grid[i][j] and not grid[j][i]:
            count += 1
    print(count)