from copy import deepcopy
N = int(input())
grid =[list(map(int,input().split())) for _ in range(N)]

def up(grid):
    for j in range(N):
        stack = []
        stop = False
        for i in range(N):
            if grid[i][j] != 0:
                if stack and stack[-1] == grid[i][j] and not stop:
                    stack[-1] *= 2
                    stop = True
                else:
                    stack.append(grid[i][j])
                    stop = False
            grid[i][j] = 0
        for i, s in enumerate(stack):
            grid[i][j] = s
def updown(grid):
    grid.reverse()
def down(grid):
    updown(grid)
    up(grid)
    updown(grid)
def transpose(grid):
    for i in range(N):
        for j in range(i+1, N):
            grid[i][j], grid[j][i] = grid[j][i], grid[i][j] 
def left(grid):
    transpose(grid)
    up(grid)
    transpose(grid)
def right(grid):
    transpose(grid)
    down(grid)
    transpose(grid)

def max2d(grid):
    return max(map(max, grid))
ans = 2

def dfs(i, grid):
    global ans
    if i==5: 
        ans = max(ans, max2d(grid))
        return

    grid0 = deepcopy(grid)    
    up(grid)
    dfs(i+1, grid)
    grid = grid0
    
    grid0 = deepcopy(grid)    
    down(grid)
    dfs(i+1, grid)
    grid = grid0
    
    grid0 = deepcopy(grid)    
    right(grid)
    dfs(i+1, grid)
    grid = grid0
    
    grid0 = deepcopy(grid)    
    left(grid)
    dfs(i+1, grid)
    grid = grid0

def print2d():
    for g in grid:
        print(*g)
dfs(0, grid)

print(ans)    