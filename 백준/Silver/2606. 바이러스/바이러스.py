N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]

visited = [False]*(N+1)
for _ in range(M):
    i, j = map(int,input().split())
    graph[i].append(j)
    graph[j].append(i)

def dfs(i):
    global count
    for j in graph[i]:
        if not visited[j]:
            visited[j] = True
            dfs(j)
            count += 1
visited[0] = True
visited[1] = True
count = 0
dfs(1)
print(count)
    
   