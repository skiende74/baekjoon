INF = 10**9

N = int(input())
M = int(input())
graph = [[INF for _ in range(N+1)] for _ in range(N+1)]

for _ in range(M):
    i,j,c = map(int, input().split())
    graph[i][j] = min(graph[i][j], c)

for i in range(1,N+1):
    graph[i][i] = 0
for k in range(1,N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

for i in range(1, N+1):
    for j in range(1, N+1):
        if graph[i][j] == INF:
            graph[i][j] = 0

for i in range(1,N+1):
    print(' '.join(map(str, graph[i][1:])))