
from collections import deque


def bfs(start):
    Q = deque(start)
    while Q:
        i,j,k,d = Q.popleft()
        grid[k][i][j] = '#'
        for di,dj,dk in zip([0,0,0,0,-1,1],[0,0,-1,1,0,0],[-1,1,0,0,0,0]):
            i2, j2, k2 = i+di, j+dj, k+dk
            if not(0<=i2<N and 0<=j2<M and 0<=k2<K) or grid[k2][i2][j2] == '#': continue
            if grid[k2][i2][j2] == 'E': return f'Escaped in {d+1} minute(s).'
            grid[k2][i2][j2] = '#'
            Q.append((i2,j2,k2,d+1))
    return 'Trapped!'

while True:
    K, N, M = map(int,input().split())
    if (K, N, M) == (0, 0, 0): break
    grid = []
    for _ in range(K):
        grid.append([list(input()) for _ in range(N)])
        input()

    Q = [ (i,j,k,0) 
        for i in range(N)
        for j in range(M)
        for k in range(K)
        if grid[k][i][j] == 'S'
        ]

    print(bfs(Q))