import sys
input = sys.stdin.readline

N, M = map(int,input().split())
grid = [list(input()) for _ in range(N)]

parent = {(i,j):(i,j) for j in range(M) for i in range(N)}
def union(i,j):
    r1,r2 = find(i),find(j)
    parent[r1]=min(r1,r2)
    parent[r2]=min(r1,r2)
def find(i):
    if parent[i]==i: return i
    parent[i] = find(parent[i])
    return parent[i]
dir = {'L':[0,-1],'R':[0,1],'D':[1,0],'U':[-1,0]}
for i in range(N):
    for j in range(M):
        di,dj = dir[grid[i][j]]
        i2,j2 = i+di, j+dj

        if not(0<=i2<N and 0<=j2<M): continue
        union((i,j),(i2,j2))
for i in range(N):
    for j in range(M):
        find((i,j))

print(len(set(parent.values())))