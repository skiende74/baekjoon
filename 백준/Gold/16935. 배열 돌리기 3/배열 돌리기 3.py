def flip_ud(grid): return grid[::-1]
def flip_lr(grid): return list(map(lambda r: r[::-1], grid))
def rotate(grid): return flip_ud(transpose(grid))
def rotate_rev(grid): return transpose(flip_ud(grid))

def transpose(grid): return list(map(list, zip(*grid)))
def op5(grid):
    N, M = len(grid), len(grid[0])
    res = [r.copy() for r in grid]
    for i in range(N//2):
        res[i][M//2:] = grid[i][:M//2]
        res[i][:M//2] = grid[i+N//2][:M//2]
    for i in range(N//2, N):
        res[i][:M//2] = grid[i][M//2:]
        res[i][M//2:] = grid[i-N//2][M//2:]
    return res

def op6(grid):
    N, M = len(grid), len(grid[0])
    res = [r.copy() for r in grid]
    for i in range(N//2):
        res[i][:M//2] = grid[i][M//2:]
        res[i][M//2:] = grid[i+N//2][M//2:]
    for i in range(N//2, N):
        res[i][:M//2] = grid[i-N//2][:M//2]
        res[i][M//2:] = grid[i][:M//2]
    return res

def print2d(grid):
    for r in grid:
        print(' '.join(map(str, r)))

N,M,R = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(N)]
op_nums = list(map(int,input().split()))

ops = {1:flip_ud, 2:flip_lr, 3:rotate_rev, 4:rotate, 5:op5, 6:op6}
for n in op_nums:  grid = ops[n](grid)
print2d(grid)
