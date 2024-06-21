N, M, T = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(N)]

def diffuse():
    grid_ = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if grid[i][j] >0:
                adj = [[i+di,j+dj] for di,dj in zip([0,0,-1,1],[-1,1,0,0]) 
                 if 0<=i+di<N and 0<=j+dj<M and grid[i+di][j+dj] >= 0]
                for i2, j2 in adj:
                    grid_[i2][j2] += grid[i][j]//5
                grid_[i][j] += grid[i][j] - grid[i][j]//5*len(adj)
            if grid[i][j] == -1: grid_[i][j] = -1
    return grid_

def circulate():
    c = [i for i in range(N) if grid[i][0] == -1][0]
    
    for i in range(1, c)[::-1]: grid[i][0] = grid[i-1][0]
    for j in range(M-1): grid[0][j] = grid[0][j+1]
    for i in range(c): grid[i][-1] = grid[i+1][-1]
    for j in range(2, M)[::-1]: grid[c][j] = grid[c][j-1]
    grid[c][1] = 0
    
    c += 1
    for i in range(c+1, N-1): grid[i][0] = grid[i+1][0]
    for j in range(M-1): grid[-1][j] = grid[-1][j+1]
    for i in range(c+1, N)[::-1]: grid[i][-1] = grid[i-1][-1]
    for j in range(2, M)[::-1]: grid[c][j] = grid[c][j-1]
    grid[c][1] = 0

def print2d():
    print('-'*40)
    for g in grid:
        print(*g)
for _ in range(T):
    #print2d()
    grid = diffuse()
    #print2d()
    circulate()
    #print2d()
print(sum(map(sum, grid))+2)