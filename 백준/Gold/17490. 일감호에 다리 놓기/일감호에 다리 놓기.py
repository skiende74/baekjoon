def union(i,j):
    u, v = find(i), find(j)
    if u == v: return
    u, v = min(u,v), max(u,v)
    parent[v] = u
    cost[u] = min(cost[u], cost[v])
    cost[v] = 0

def find(i):
    if parent[i] == i: return i
    parent[i] = find(parent[i])
    return parent[i]

import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
cost = [10**9]+list(map(int,input().split()))
con = {(i, i+1) for i in range(1,N)}
con.add((1, N))

for _ in range(M):
    i, j = map(int, input().split())
    i,j = sorted((i, j))
    if (i,j) in con: con.remove((i,j))
parent = [i for i in range(N+1)]
union(0,1)

for i, j in con: union(i, j)
print('YES' if len({find(i) for i in range(N+1)})==1 or sum(cost)<=K else 'NO')