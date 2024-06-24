def search():
    global result
    for i in range(N):
        cnt = 1
        for j in range(1, N):
            if grid[i][j] == grid[i][j-1]: cnt += 1
            else: cnt = 1
            result = max(result, cnt)
    for j in range(N):
        cnt = 1
        for i in range(1, N):
            if grid[i][j] == grid[i-1][j]: cnt += 1
            else: cnt = 1
            result = max(result, cnt)

N = int(input())
grid = [list(input()) for _ in range(N)]

result = 0
for i in range(N):
    for j in range(N-1):
        if grid[i][j] == grid[i][j+1]: continue
        grid[i][j], grid[i][j+1] = grid[i][j+1],grid[i][j]
        search()        
        grid[i][j], grid[i][j+1] = grid[i][j+1],grid[i][j]
for i in range(N-1):
    for j in range(N):
        if grid[i][j] == grid[i+1][j]: continue
        grid[i][j], grid[i+1][j] = grid[i+1][j],grid[i][j]
        search()
        grid[i][j], grid[i+1][j] = grid[i+1][j],grid[i][j]
print(result)