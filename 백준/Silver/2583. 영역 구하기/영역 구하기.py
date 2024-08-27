def dfs(i,j):
    global inner_cnt
    for di, dj in zip([0,0,-1,1],[-1,1,0,0]):
        i2, j2 = i+di, j+dj
        if not (0<=i2<N and 0<=j2<M) or grid[i2][j2] == 1: continue
        if visited[i2][j2]: continue
        visited[i2][j2] = True
        inner_cnt += 1
        dfs(i2,j2)

import sys
sys.setrecursionlimit(10000+2)
input = sys.stdin.readline
N,M,K = map(int,input().split())
grid = [[0]*(M) for _ in range(N)]
for _ in range(K):
    j1,i1, j2,i2 = map(int,input().split())
    for i in range(i1,i2):
        for j in range(j1,j2):
            grid[i][j] = 1

result = []
visited = [[False]*(M) for _ in range(N)]
for i in range(N):
    for j in range(M):
        if visited[i][j] or grid[i][j] == 1: continue
        visited[i][j] = True
        inner_cnt = 1
        dfs(i, j)
        result.append(inner_cnt)
print(len(result))
print(' '.join(map(str,sorted(result))))
