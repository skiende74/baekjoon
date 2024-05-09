import sys
input = sys.stdin.readline
V = int(input())
points = [list(map(float,input().split())) for _ in range(V)]
edges = []

def dist(i,j):
    return ((points[i][0]-points[j][0])**2 + (points[i][1]-points[j][1])**2)**0.5

for i,(x, y) in enumerate(points):
    for j in range(i):
        edges.append([dist(i,j), i,j])
edges.sort()

parent = [i for i in range(V)]
def union(i,j):
    r1,r2 = find(i),find(j)
    parent[max(r1,r2)] = min(r1,r2)
def find(i):
    if parent[i] == i: return i
    parent[i] = find(parent[i])
    return parent[i]

cost = 0
for d,i,j in edges:
    if find(i) != find(j):
        union(i,j)
        cost += d
print(round(cost,2))