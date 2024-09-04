import sys
input = sys.stdin.readline
from collections import deque
from itertools import combinations
N, M = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(N)]
candis = [(i,j)
for i in range(N)
    for j in range(N)
        if grid[i][j] == 2]
count_1 = sum(map(lambda r: r.count(1), grid))
ans = 10**9
for cs in combinations(candis, M):
    dist = 0
    cnt = M

    visited = [[False]*N for _ in range(N)]
    for c in cs:
        visited[c[0]][c[1]] = True
    Q = deque([(*c, 0) for c in cs])
    while Q:
        i, j, d = Q.popleft()
        for di, dj in zip([0,0,-1,1], [-1,1,0,0]):
            i2, j2 = i+di, j+dj
            if not (0<=i2<N and 0<=j2<N) or visited[i2][j2]: continue
            visited[i2][j2] = True

            if grid[i2][j2] == 1: continue
            cnt += 1
            dist = max(dist, d+1)
            Q.append((i2,j2,d+1))
    
    if cnt + count_1  == N**2:
        ans = min(ans, dist)

print(ans if ans != 10**9 else -1)