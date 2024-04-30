import sys
input = sys.stdin.readline
V, S = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(V)]

visited =[False]*(V)
visited[S]=True
for k in range(V):
    for i in range(V):
        for j in range(V):
            grid[i][j] = min(grid[i][j], grid[i][k] + grid[k][j])

def dfs(i):
    global dist, min_dist
    if all(visited):
        min_dist = min(min_dist, dist)
    for j in range(V):
        if visited[j]: continue
        visited[j] = True
        dist += grid[i][j]
        dfs(j)
        visited[j] = False
        dist -= grid[i][j]
dist = 0
min_dist = 10**9
dfs(S)
print(min_dist)