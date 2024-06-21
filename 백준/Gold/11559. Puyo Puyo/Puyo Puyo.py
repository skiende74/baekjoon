N, M = 12, 6
grid = [list(input()) for _ in range(N)]


def boom():
    is_boom = False
    def dfs(i, j):
        nonlocal cnt
        for di, dj in zip([0,0,-1,1],[-1,1,0,0]):
            i2, j2 = i+di, j+dj
            if not(0<=i2<N and 0<=j2<M): continue
            if visited[i2][j2] or grid[i2][j2]!=c: continue
            visited[i2][j2] = True
            cnt += 1
            res.append((i2,j2))
            dfs(i2, j2)

    visited = [[False]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if visited[i][j] or grid[i][j] == '.': continue
            visited[i][j] = True
            cnt = 1
            res = [(i,j)]
            c = grid[i][j]
            dfs(i, j)
            if cnt >= 4: # 펑
                for r_i, r_j in res:
                    grid[r_i][r_j] = '.'
                is_boom = True
    return is_boom

def go_down():
    for j in range(M):
        for i in range(N):
            for i2 in range(N-1-i):
                if grid[i2][j] != '.' and grid[i2+1][j] == '.':
                    grid[i2][j], grid[i2+1][j] = grid[i2+1][j], grid[i2][j]

for k in range(10**8):
    is_boom = boom()
    go_down()
    if not is_boom: break
print(k)