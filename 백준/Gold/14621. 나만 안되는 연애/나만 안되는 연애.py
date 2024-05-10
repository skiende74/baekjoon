import sys
input = sys.stdin.readline

N, M = map(int, input().split())
types = ['A']+input().split()
edges = [ list(map(int,input().split())) for  _ in range(M)]
edges.sort(key=lambda x:x[2])

parent = [i for i in range(N+1)]
def union(i,j):
    r1,r2 = find(i), find(j)
    parent[max(r1,r2)] = min(r1,r2)
def find(i):
    if parent[i] == i: return i
    parent[i] = find(parent[i])
    return parent[i]


cost, cnt = 0, 0
for i, j, d in edges:
    if find(i) != find(j) and types[i] != types[j]:
        union(i,j)
        cost += d
        cnt += 1
print(cost if cnt == N-1 else -1)