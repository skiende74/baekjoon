from collections import deque

def bfs(start):
    Q = deque(start)
    while Q:
        i, d = Q.popleft()
        if i == E: return d
        for j in graph[i]:
            if visited[j]: continue
            visited[j] = True
            Q.append((j,d+1))
    return -1

N = int(input())
S, E = map(int,input().split())
visited = [False]*(N+1)
visited[S] = True
graph = [[] for _ in range(N+1)]
for _ in range(int(input())):
    i, j = map(int,input().split())
    graph[i].append(j)
    graph[j].append(i)

print(bfs([(S, 0)]))