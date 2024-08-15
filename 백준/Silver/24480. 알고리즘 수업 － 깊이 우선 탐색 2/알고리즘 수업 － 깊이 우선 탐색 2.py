def dfs(i):
    global cnt
    for j in graph[i]:
        if visited[j]: continue
        visited[j] = cnt
        cnt += 1
        dfs(j)
import sys
sys.setrecursionlimit(10**5+1)
input = sys.stdin.readline
V, E, S = map(int,input().split())
visited = [0]*(V+1)
graph = [[] for _ in range(V+1)]

for _ in range(E):
    i , j = map(int,input().split())
    graph[i].append(j)
    graph[j].append(i)
for i in range(1,V+1):
    graph[i].sort(reverse=True)
cnt = 2
visited[S] = 1
dfs(S)
print(*visited[1:], sep='\n')