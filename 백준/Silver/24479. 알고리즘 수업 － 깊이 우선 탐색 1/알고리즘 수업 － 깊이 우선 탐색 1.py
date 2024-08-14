import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5+1)

V, E, S = map(int,input().split())

def dfs(i):
    global c
    visited[i] = c
    c += 1
    for j in graph[i]:
        if visited[j]: continue
        dfs(j)

graph = [[] for _ in range(V+1)]
visited = [0]*(V+1)
edges = [list(map(int,input().split())) for _ in range(E)]
edges.sort()
for i, j in edges:
    graph[i].append(j)
    graph[j].append(i)
c = 1
dfs(S)
for i in range(1,V+1):
    print(visited[i])