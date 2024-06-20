N, M, K = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(N)]

def print2d():
    for g in grid:
        print(*g)

for k in range(min(N,M)//2):
    mod = ((N+M-2-4*k)*2)
    if mod == 0: continue
    for _ in range(K%mod):
        tmp = grid[k][k]

        grid[k][k:-1-k] = grid[k][k+1:M-k]
        for i in range(k+1, N-k):
            grid[i-1][-1-k] = grid[i][-1-k]

        grid[-1-k][k+1:M-k] = grid[-1-k][k:-1-k]
        for i in range(k+2, N-k)[::-1]:
            grid[i][k] = grid[i-1][k]

        grid[1+k][k] = tmp
print2d()