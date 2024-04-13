from heapq import heappush, heappop

M, N = map(int,input().split())
grid = [[0]*(M+1)]+[[0]+list(map(int, list(input()))) for _ in range(N)]

INF = 10**9
dist = [[INF]*(M+1) for _ in range(N+1)]
dist[1][1] = 0
PQ = [(0, (1, 1))]
while PQ:
    d, (i,j) = heappop(PQ)

    for di, dj in zip([0,0,-1,1],[-1,1,0,0]):
        i2, j2 = i+di, j+dj
        if not(1<=i2<=N and 1<=j2<=M): continue
        if dist[i2][j2] > d+grid[i2][j2]:
            dist[i2][j2] = d+grid[i2][j2]
            heappush(PQ, (dist[i2][j2], (i2,j2)))
print(dist[-1][-1])