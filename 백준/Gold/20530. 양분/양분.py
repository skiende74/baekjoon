
def dfs(i):
    global path
    if path: return
    if i == goal:
        path = path0.copy()
        return
    for j in graph[i]:
        if visited[j]: continue
        visited[j] = True

        path0.append(j)
        dfs(j)
        path0.pop()

def union(i, j):
    u, v = find(i), find(j)
    u, v = min(u, v), max(u, v)
    parent[v] = u

def find(i):
    if parent[i] == i: return i
    parent[i] = find(parent[i])
    return parent[i]

import sys
sys.setrecursionlimit(3*10**5)
input = sys.stdin.readline
N, Q = map(int,input().split())

visited = [False]*(N+1)
edges = [list(map(int,input().split())) for _ in range(N)]
graph = [[] for _ in range(N+1)]
for i, j in edges:
    graph[i].append(j)
    graph[j].append(i)

parent = [ i for i in range(N+1)]
for i, j in edges:
    if find(i) != find(j): union(i, j)
    else:
        goal = j
        path, path0 = [], [i]
        visited[i] = True
        dfs(i)
path = set(path)

visited = [ i in path for i in range(N+1)]
group = [i for i in range(N+1)]
for i0 in path:    
    stack = [i0]
    while stack:
        i = stack.pop()
        for j in graph[i]:
            if visited[j]: continue
            visited[j] = True
            group[j] = i0
            stack.append(j)

for _ in range(Q):
    i, j = map(int,input().split())
    print(1 + (group[i] != group[j]))