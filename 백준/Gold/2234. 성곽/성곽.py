di,dj =  [0,-1,0,1], [-1,0,1,0]
def dfs(i, j):
    global cnt
    for k in range(4):
        if (grid[i][j] & 1<<k): continue
        i2, j2 = i+di[k], j+dj[k]
        if not (0<=i2<N and 0<=j2<M) or visited[i2][j2]: continue
        visited[i2][j2] = True
        marker[i2][j2] = l
        cnt += 1
        dfs(i2, j2)

import sys
sys.setrecursionlimit(10**4)
input = sys.stdin.readline
M, N = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(N)]
marker = [[0]*M for _ in range(N)]
inner_cnt = dict()

visited = [[False]*M for _ in range(N)]        
l = 0
for i in range(N):
    for j in range(M):
        if visited[i][j]: continue
        visited[i][j] = True
        cnt = 1
        marker[i][j] = l
        dfs(i,j)
        
        inner_cnt[l] = cnt
        l += 1

ans = 0
for i in range(N):
    for j in range(M):
        for k in range(4):
            if not(grid[i][j] & 1<<k): continue
            i2, j2 = i+di[k], j+dj[k]
            if not(0<=i2<N and 0<=j2<M) or marker[i][j] == marker[i2][j2]: continue
            ans = max(ans, inner_cnt[marker[i][j]] + inner_cnt[marker[i2][j2]])
print(l, max(inner_cnt.values()), ans, sep='\n')