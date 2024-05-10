import sys
input = sys.stdin.readline
N = int(input())
grid = [list(map(int,input().split())) for _ in range(N)]
edges = [ (grid[i][j],i,j) for i in range(N) for j in range(i+1, N)]
edges.sort()

parent = [i for i in range(N+1)]
def union(i,j):
    r1,r2 = find(i), find(j)
    parent[max(r1,r2)] = min(r1,r2)
def find(i):
    if parent[i] == i: return i
    parent[i] = find(parent[i])
    return parent[i]

cost = 0
for d,i,j in edges:
    if find(i) != find(j):
        cost += d
        union(i,j)
print(cost)