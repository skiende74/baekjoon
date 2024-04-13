from heapq import heappush, heappop
N = int(input())
k=1
while N != 0:
    grid = [list(map(int, input().split())) for _ in range(N)]

    INF = 10**9
    dist = [[INF]*N for _ in range(N)]
    dist[0][0] = grid[0][0]
    PQ = [(dist[0][0], (0,0))]
    while PQ:
        d, (i, j) = heappop(PQ)

        for di, dj in zip([0,0,-1,1],[-1,1,0,0]):
            i2, j2 = i+di, j+dj
            if 0<=i2<N and 0<=j2<N and dist[i2][j2] > d+grid[i2][j2]:
                dist[i2][j2] = d + grid[i2][j2]
                heappush(PQ, (dist[i2][j2], (i2, j2)))
    print(f'Problem {k}: {dist[-1][-1]}')
    k += 1
    N = int(input())