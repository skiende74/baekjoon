
from collections import deque

def bfs():
    Q = deque([])
    day = 0
    for i in range(N):
        for j in range(M):
            for k in range(H):
                if grid_3d[k][i][j] == 1:
                    Q.append((i,j,k,0))
    while Q:
        i,j,k,day = Q.popleft()
        for di,dj,dk in zip([0,0,0,0,-1,1],[0,0,-1,1,0,0],[-1,1,0,0,0,0]):
            i2,j2,k2 = i+di, j+dj, k+dk
            if not(0<=i2<N and 0<=j2<M and 0<=k2<H): continue
            if visited[i2][j2][k2]: continue
            if grid_3d[k2][i2][j2] != 0: continue
            visited[i2][j2][k2] = True
            grid_3d[k2][i2][j2] = 1
            Q.append((i2,j2,k2,day+1))
    return day

import sys
input = lambda: sys.stdin.readline().rstrip()
M, N, H = map(int, input().split())
grid_3d = [[list(map(int,input().split())) for _ in range(N)] for _ in range(H)]
visited=[[[False]*H for _ in range(M)] for _ in range(N)]

ans = bfs()
for i in range(N):
    for j in range(M):
        for k in range(H):
            if grid_3d[k][i][j] == 0:
                ans = -1
print(ans)