from collections import deque

def bfs(i,j):
    Q = deque([(i,j)])
    melt = []
    while Q:
        i,j = Q.popleft()
        if visited[i][j]: continue
        visited[i][j] = True
        n = 0
        for di, dj in zip([0,0,-1,1],[-1,1,0,0]):
            i2, j2 = i+di, j+dj
            if not (0<=i2<N and 0<=j2<M): continue
            if grid[i2][j2] == 0: n+=1
            if visited[i2][j2] or grid[i2][j2]==0: continue
            Q.append((i2, j2))
        if n>0: melt.append((i, j, max(0, grid[i][j]-n)))
    for i,j,v in melt: grid[i][j] = v

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
            cnt += 1
            bfs(i,j)

    if cnt>1: 
        print(k-1)
        break
    if cnt == 0:
        print(0)
        break