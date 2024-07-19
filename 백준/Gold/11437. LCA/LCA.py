prev = -1
def dfs(i):
    global prev
    for j in graph[i]:
        if depth[j] != 10**9: continue
        parent[j] = i
        depth[j] = depth[i] + 1    
        dfs(j)
        

def lca(i, j):
    while depth[i] > depth[j]: i = parent[i]
    while depth[i] < depth[j]: j = parent[j]
    while i != j: i, j = parent[i], parent[j]
    return i

import sys
sys.setrecursionlimit(50000+1)
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]
for i, j in  [list(map(int,input().split())) for _ in range(N-1)]:
    graph[i].append(j)
    graph[j].append(i)

parent = [i for i in range(N+1)]
depth = [10**9]*(N+1)

depth[1] = 0
dfs(1)
for _ in range(int(input())):
    i, j = map(int,input().split())
    print(lca(i,j))