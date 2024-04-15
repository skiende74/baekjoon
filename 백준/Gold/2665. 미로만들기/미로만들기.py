from heapq import heappop, heappush
import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
grid = [ list(map(int, list(input()))) for _ in range(N)]
for i in range(N):
    for j in range(N):
        grid[i][j] = 1-grid[i][j]

INF = 10**9
dist = [ [INF]*N for _ in range(N)]
dist[0][0] = 0

st = 0
PQ = [(0, (0,0))]

while PQ:
    d, (i,j) = heappop(PQ)

    for di, dj in zip([0,0,-1,1],[-1,1,0,0]):
        i2, j2 = i+di, j+dj
        if 0<=i2<N and 0<=j2<N and dist[i2][j2] > d+grid[i2][j2]:
            dist[i2][j2] = d+grid[i2][j2]
            heappush(PQ, (dist[i2][j2], (i2,j2)))

print(dist[-1][-1])