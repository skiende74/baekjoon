import sys
sys.setrecursionlimit(2**12+4)
input = lambda: sys.stdin.readline().rstrip()
def rotate(i0,j0, l):
    for i in range(l):
        grid[i0+i][j0:j0+l] = list(reversed(grid_tr[j0+i][i0:i0+l]))

def rotate_step(L):
    l = 2**L
    for i in range(0, N, l):
        for j in range(0, N, l):
            rotate(i,j,l)

def decrease():
    global grid
    grid_ = [row.copy() for row in grid]
    for i in range(N):
        for j in range(N):
            adj = ['' for di,dj in zip([0,0,-1,1],[-1,1,0,0])
                   if 0<=i+di<N and 0<=j+dj<N and grid[i+di][j+dj]>0]
            if len(adj)<3: grid_[i][j] = max(0, grid[i][j]-1)
    grid = grid_
    
def count_max():
    visited = [[False]*N for _ in range(N)]
    def dfs(i,j):
        nonlocal visited, inner_cnt
        for di, dj in zip([0,0,-1,1],[-1,1,0,0]):
            i2, j2 = i+di, j+dj
            if not(0<=i2<N) or not(0<=j2<N) or visited[i2][j2] or grid[i2][j2]==0: continue
            visited[i2][j2] = True
            inner_cnt += 1
            dfs(i2,j2)

    max_inner = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] or grid[i][j]==0: continue
            visited[i][j] = True
            inner_cnt = 1
            dfs(i,j)
            max_inner = max(max_inner, inner_cnt)
    return max_inner

n, Q = map(int,input().split())
N = 2**n

grid = [list(map(int,input().split())) for _ in range(N)]
steps = list(map(int,input().split()))

for step in steps:
    grid_tr = list(zip(*grid))
    rotate_step(step)
    decrease()

M = max(map(max, grid))
print(sum(map(sum, grid)))
print(count_max())