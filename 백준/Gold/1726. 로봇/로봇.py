from heapq import heappop, heappush

left = {1:4,2:3,3:1,4:2}
right = {1:3,2:4,3:2,4:1}

didj = {1:(0,1),2:(0,-1),3:(1,0),4:(-1,0)}

def can_move(i,j):
    return 1<=i<=N and 1<=j<=M and grid[i][j] == 0

def bfs(i,j, dir):
    PQ = [(0, i,j,dir)]

    while PQ:
        d, i,j,dir = heappop(PQ)
        if (i,j, dir) == (g_i,g_j,g_dir): return
        if can_move(i,j) and dist[i][j][left[dir]] > d+1:
            dist[i][j][left[dir]] = d+1
            heappush(PQ, (d+1, i,j,left[dir]))
        if can_move(i,j) and dist[i][j][right[dir]] > d+1:
            dist[i][j][right[dir]] = d+1
            heappush(PQ, (d+1, i,j,right[dir]))

        di,dj = didj[dir]
        i2,j2 = i, j
        for _ in range(3):
            i2, j2 = i2+di, j2+dj
            if not can_move(i2, j2): break
            if not (dist[i2][j2][dir] > d+1): continue
            dist[i2][j2][dir] = d+1
            heappush(PQ, (d+1, i2,j2,dir))
        

import sys
input = sys.stdin.readline
N, M = map(int,input().split())
grid = [[1]*(M+1)] +[[1]+list(map(int,input().split())) for _ in range(N)]
i,j,dir = map(int,input().split())
g_i, g_j, g_dir = map(int,input().split())

dist = [[[10**9]*5 for _ in range(M+1)] for _ in range(N+1)]
dist[i][j][dir] = 0
bfs(i,j,dir)
print(dist[g_i][g_j][g_dir])