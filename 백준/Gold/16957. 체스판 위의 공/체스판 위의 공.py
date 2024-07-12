import sys
input = sys.stdin.readline
def union(x1,x2):
    r1, r2 = find(x1), find(x2)
    if grid[r1[0]][r1[1]] > grid[r2[0]][r2[1]]: r1, r2 = r2, r1
    
    if r1 == r2: return
    count[r1[0]][r1[1]] += count[r2[0]][r2[1]]
    count[r2[0]][r2[1]] = 0
    parent[r2[0]][r2[1]] = r1

def find(r):
    if parent[r[0]][r[1]] == r: return r
    parent[r[0]][r[1]] = find(parent[r[0]][r[1]])
    return parent[r[0]][r[1]]

N, M = map(int,input().split())
parent = [[ (i,j) for j in range(M)] for i in range(N)]
count = [[ 1 for _ in range(M)] for _ in range(N)]
grid = [list(map(int,input().split())) for _ in range(N)]

for i in range(N):
    for j in range(M):
        _,i2,j2 = min([(grid[i2][j2],i2,j2)for i2 in range(i-1,i+2) for j2 in range(j-1, j+2) if 0<=i2<N and 0<=j2<M])
        union((i,j),(i2,j2))

for i in range(N):
    print(' '.join(map(str, count[i])))