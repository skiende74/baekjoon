from copy import deepcopy
N = int(input())
grid =[list(map(int,input().split())) for _ in range(N)]

def up():
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
def updown():
    grid.reverse()
def down():
    updown()
    up()
    updown()
def transpose():
    global grid
    grid = list(map(list, zip(*grid)))

def left():
    transpose()
    up()
    transpose()
def right():
    transpose()
    down()
    transpose()

def max2d(grid):
    return max(map(max, grid))
ans = 2

def dfs(i):
    global grid, ans
    if i==5: 
        ans = max(ans, max2d(grid))
        return

    grid0 = deepcopy(grid)    
    up()
    dfs(i+1)
    grid = grid0
    
    grid0 = deepcopy(grid)    
    down()
    dfs(i+1)
    grid = grid0
    
    grid0 = deepcopy(grid)    
    right()
    dfs(i+1)
    grid = grid0
    
    grid0 = deepcopy(grid)    
    left()
    dfs(i+1)
    grid = grid0

dfs(0)
print(ans)    