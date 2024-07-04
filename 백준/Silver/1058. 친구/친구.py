N = int(input())
graph = [ list(map(lambda x: 1 if x=='Y' else 0, list(input()))) for _ in range(N) ]

for k in range(N):
    for i in range(N):
        for j in range(N):
            if i==j: continue
            if graph[i][j]: continue
            if graph[i][k]==1 and graph[k][j]==1: graph[i][j] = 2
for i in range(N):
    for j in range(N):
        if graph[i][j]: graph[i][j] = 1
print(max(map(sum, graph)))
