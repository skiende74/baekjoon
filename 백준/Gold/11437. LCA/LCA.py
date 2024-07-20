def dfs(i):
    for j in graph[i]:
        if depth[j] != 10**9: continue
        depth[j] = depth[i] + 1
        parent[j] = i
        dfs(j)

def lca(i, j):
    while depth[i] > depth[j] : i = parent[i]
    while depth[i] < depth[j] : j = parent[j]
    while i != j: i, j = parent[i], parent[j]
    return i
    
import sys
sys.setrecursionlimit(50000+1)
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

depth = [10**9]*(N+1)
parent = [0]*(N+1)

depth[1] = 0
parent[1] = 1
dfs(1)
for _ in range(int(input())):
    print(lca(*map(int, input().split())))