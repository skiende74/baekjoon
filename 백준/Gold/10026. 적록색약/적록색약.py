import sys
sys.setrecursionlimit(10**5)

N = int(input())
grid = [list(input()) for _ in range(N)]
color_id1 = {'R':0,'G':1,'B':2}
color_id2 = {'R':0,'G':0,'B':2}

def dfs(i,j):
    for di, dj in zip([0,0,-1,1],[-1,1,0,0]):
        i2, j2 = i+di, j+dj
        
        if 0<=i2<N and 0<=j2<N and not visited[i2][j2] and color_id[grid[i][j]] == color_id[grid[i2][j2]]:
            visited[i2][j2] = True
            dfs(i2,j2)

color_id = color_id1
outer_count = 0
visited = [[False]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[i][j]:   
            outer_count += 1
            dfs(i,j)
print(outer_count, end=' ')
outer_count = 0
visited = [[False]*N for _ in range(N)]
color_id = color_id2
for i in range(N):
    for j in range(N):
        if not visited[i][j]:   
            outer_count += 1
            dfs(i,j)

print(outer_count)