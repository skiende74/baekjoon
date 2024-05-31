import sys
input = sys.stdin.readline

N, M = map(int,input().split())

graph = [[] for _ in range(N)]
for _ in range(M):
    i, j = map(int,input().split())
    graph[i].append(j)
    graph[j].append(i)

ans = 0
cnt = 0
visited = [False]*N
def dfs(i):
    global cnt, ans    
    if cnt == 4:
        ans = 1
        return
    for j in graph[i]:
        if visited[j]: continue
        cnt += 1
        visited[j] = True
        dfs(j)
        visited[j] = False
        cnt -= 1
for i in range(N):
    visited[i] = True
    dfs(i)
    visited[i] = False
print(ans)