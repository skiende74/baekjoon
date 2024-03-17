R, C = map(int, input().split())
grid = [list(input()) for _ in range(R)]

def dfs(i,j):
    global inner_count, max_inner_count
    for di, dj in zip([0,0,-1,1], [-1,1,0,0]):
        i2, j2 = i+di, j+dj
        if 0<=i2<R and 0<=j2<C and not visited2[ord(grid[i2][j2])-65]:
            visited2[ord(grid[i2][j2])-65] = True
            inner_count += 1
            max_inner_count = max(max_inner_count, inner_count)
            dfs(i2, j2)
            inner_count -= 1
            visited2[ord(grid[i2][j2])-65] = False

visited = {grid[0][0]}
visited2 = [False]*26
visited2[ord(grid[0][0]) - 65] = True
inner_count = 1
max_inner_count = 1
dfs(0,0)
print(max_inner_count)