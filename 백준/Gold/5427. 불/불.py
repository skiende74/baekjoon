from collections import deque

def bfs(start):
    Q = deque(start)

    while Q:
        i,j,F,d =Q.popleft()
        for di, dj in zip([0,0,-1,1],[-1,1,0,0]):
            i2, j2 = i+di, j+dj
            if not(0<=i2<N and 0<=j2<M) or grid[i2][j2] != '.': continue
            grid[i2][j2] = F
            Q.append((i2,j2,F, d+1))
            if F=='@' and (i2==0 or i2==N-1 or j2 == 0 or j2==M-1): return d+1
    return 'IMPOSSIBLE'

import sys
input = sys.stdin.readline
for _ in range(int(input())):
    M, N = map(int,input().split())
    grid = [list(input()) for _ in range(N)]
    Q = []
    for i in range(N):
        for j in range(M):
            if grid[i][j] == '*':
                Q.append((i,j,'*', 1))
    for i in range(N):
        for j in range(M):
            if grid[i][j] == '@':
                Q.append((i,j,'@', 1))
    i, j,F,d = Q[-1]
    if (i==0 or i==N-1 or j == 0 or j==M-1) and F=='@':
        print(1)
    else: print(bfs(Q))