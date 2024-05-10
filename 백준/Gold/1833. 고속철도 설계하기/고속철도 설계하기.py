import sys
input= sys.stdin.readline
N = int(input())
grid = [list(map(int,input().split())) for _ in range(N)]

parent = [i for i in range(N+1)]
def union(i,j):
    r1,r2 = find(i),find(j)
    parent[max(r1,r2)] = min(r1,r2)
def find(i):
    if parent[i] == i: return i
    parent[i] = find(parent[i])
    return parent[i]

edges = []
cost = 0
for i in range(N):
    for j in range(i+1,N):
        if grid[i][j]<0:
            union(i,j)
            cost += -grid[i][j]
        if grid[i][j]>0:
            edges.append((grid[i][j],i,j))

edges.sort()
cnt = 0
roads =[]
for d,i,j in edges:
    if find(i) != find(j):
        union(i,j)
        cost += d
        cnt += 1
        roads.append((i,j))
print(cost, cnt)
for i,j in roads:
    print(i+1, j+1)