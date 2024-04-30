import sys
input = sys.stdin.readline
V, E = int(input()), int(input())

INF = 10**9
grid = [[INF]*(V+1) for _ in range(V+1)]
for i in range(1,V+1): grid[i][i] = 0
for _ in range(E):
    i,j = map(int,input().split())
    grid[i][j] = 1
    grid[j][i] = 1

for k in range(1, V+1):
    for i in range(1, V+1):
        for j in range(1, V+1):
            grid[i][j] = min(grid[i][j], grid[i][k] + grid[k][j])

def max2(arr):
    return max( [a for a in arr if a!= INF])

ans = []
visited = [False]*(V+1)
for i in range(1, V+1):
    if visited[i]: continue
    visited[i] = True
    group = [i]
    for j in range(1, V+1):
        if visited[j]: continue
        if grid[i][j] == INF: continue
        visited[j] = True
        group.append(j)
        
    min_max = min([max2(grid[g]) for g in group])
    g2 = [max2(grid[g]) for g in group].index(min_max)
    ans.append(group[g2])
print(len(ans))
print(*sorted(ans), sep='\n')