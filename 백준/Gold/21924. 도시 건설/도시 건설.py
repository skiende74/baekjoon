import sys
input = sys.stdin.readline

V, E = map(int,input().split())
edges = [list(map(int,input().split())) for _ in range(E)]
edges.sort(key=lambda x: x[2])

parent = [i for i in range(V+1)]
def union(i,j):
    r1,r2 = find(i), find(j)
    parent[max(r1,r2)] = min(r1,r2)
def find(i):
    if parent[i] == i: return i
    parent[i] = find(parent[i])
    return parent[i]

cost0=sum(map(lambda x: x[2], edges))

cost = 0
cnt = 0
for i,j,d in edges:
    if find(i) != find(j):
        union(i,j)
        cost += d
        cnt += 1

print(cost0-cost if cnt == V-1 else -1)