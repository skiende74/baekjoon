import sys
sys.setrecursionlimit(10**5)

def dfs(i,j):
    for di in range(-1,1+1):
        for dj in range(-1,1+1):
            i2, j2= i+di, j+dj
            if 0<=i2<h and 0<=j2<w and grid[i2][j2] == 1 and not visited[i2][j2]:
                visited[i2][j2] = True
                dfs(i2,j2)
while True:
    w, h = map(int, input().split())
    if (w,h) == (0,0):
        break
    grid = [list(map(int,input().split())) for _ in range(h)]
    outer_count = 0
    visited = [[False]*(w) for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 1 and not visited[i][j]:
                visited[i][j] = True
                outer_count += 1
                dfs(i, j)
    print(outer_count)