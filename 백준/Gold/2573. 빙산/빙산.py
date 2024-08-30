
from collections import deque

def bfs(i,j):
    Q = deque([(i,j)])
    grid0 = [r.copy() for r in grid]
    while Q:
        i,j = Q.popleft()
        sea_points = [(i+di, j+dj) for di, dj in zip([0,0,-1,1],[-1,1,0,0]) if 0<=i+di<N and 0<=j+dj<M and grid0[i+di][j+dj] == 0]
        grid[i][j] = max(0, grid0[i][j]-len(sea_points))

        for di, dj in zip([0,0,-1,1],[-1,1,0,0]):
            i2, j2 = i+di, j+dj
            if not (0<=i2<N and 0<=j2<M): continue
            if visited[i2][j2] or grid0[i2][j2]==0: continue
            visited[i2][j2] = True
            Q.append((i2, j2))
    # print(*grid)

def bfs_check(i,j):
    Q = deque([(i,j)])
    while Q:
        i,j = Q.popleft()
        for di, dj in zip([0,0,-1,1],[-1,1,0,0]):
            i2, j2 = i+di, j+dj
            if not (0<=i2<N and 0<=j2<M): continue
            if visited[i2][j2] or grid[i2][j2] == 0: continue
            visited[i2][j2] = True
            Q.append((i2, j2))

import sys
input = sys.stdin.readline
N, M =map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(N) ]
visited = [[False]*(M) for _ in range(N) ]


for k in range(1, N*M+1):
    cnt = 0
    visited = [[False]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if visited[i][j] or grid[i][j] == 0: continue
            visited[i][j] = True
            cnt += 1
            bfs(i,j)

    if cnt>1: 
        print(k-1)
        break
else: print(0)