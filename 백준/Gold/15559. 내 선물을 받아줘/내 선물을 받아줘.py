def union(r1, r2):
    r1, r2 = find(r1), find(r2)
    r1, r2 = min(r1,r2), max(r1,r2)
    i1,j1 = r1
    i2,j2 = r2
    parent[i2][j2] = i1,j1

def find(r):
    i,j = r
    if parent[i][j] == r: return r
    parent[i][j] = find(parent[i][j])
    return parent[i][j]

import sys
input = lambda: sys.stdin.readline().rstrip()
N, M = map(int,input().split())
grid = [list(input()) for _ in range(N)]
dir = {'N': (-1,0), 'S': (1,0), 'E': (0, 1), 'W': (0, -1)}
visited = [[False]*M for _ in range(N)]
parent = [[ (i,j) for j in range(M)] for i in range(N)]
cnt = 0
for i in range(N):
    for j in range(M):
        di,dj = dir[grid[i][j]]
        i2, j2 = i+di, j+dj
        union((i,j),(i2,j2))
        cnt += 1

print(len({find((i,j))
for i in range(N)
    for j in range(M)}))
