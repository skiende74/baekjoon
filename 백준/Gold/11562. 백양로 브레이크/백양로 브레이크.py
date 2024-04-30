import sys
input = sys.stdin.readline
V, E = map(int,input().split())
INF = 10**9
grid = [[INF]*(V+1) for _ in range(V+1)]
for i in range(1,V+1): grid[i][i]= 0
candidates = []
for _ in range(E):
    i,j,b = map(int,input().split())
    grid[i][j] = 0
    if b==1: grid[j][i]=0
    else: grid[j][i] = 1

for k in range(1,V+1):
    for i in range(1,V+1):
        for j in range(1,V+1):
            grid[i][j] = min(grid[i][j], grid[i][k]+grid[k][j])

for _ in range(int(input())):
    s, e = map(int,input().split())
    print(grid[s][e])