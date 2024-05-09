import sys
input = sys.stdin.readline
V = int(input())
E = int(input())
edges = [list(map(int,input().split())) for _ in range(E)]
edges.sort(key=lambda x: x[2])

parent = [i for i in range(V+1)]
def union(i,j):
    r1, r2 = find(i), find(j)
    parent[max(r1,r2)] = min(r1,r2)
def find(i):
    if parent[i] == i: return i
    parent[i] = find(parent[i])
    return parent[i]

cost = 0
for i,j,w in edges:
    if find(i) != find(j):
        union(i,j)
        cost += w
print(cost)