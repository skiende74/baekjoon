import sys
input = sys.stdin.readline
N = int(input())
W = [0]+[int(input()) for _ in range(N)]
grid = [[0]*(N+1)]+[[0]+list(map(int,input().split())) for _ in range(N)]

parent = [i for i in range(N+1)]
def union(i,j):
    r1,r2 = find(i), find(j)
    parent[max(r1,r2)] = min(r1,r2)
def find(i):
    if parent[i] == i: return i
    parent[i] = find(parent[i])
    return parent[i]

for j in range(1, N+1):
    grid[0][j] = W[j]

edges = []
for i in range(N+1):
    for j in range(i+1, N+1):
        edges.append((grid[i][j],i,j))
edges.sort()

cost = 0
for d,i,j in edges:
    if find(i) != find(j):
        union(i,j)
        cost += d
print(cost)