from collections import deque
import sys
input =sys.stdin.readline

V, E = map(int,input().split())

indegree = [0]*(V+1)
graph = [[] for _ in range(V+1)]
for _ in range(E):
    _, *edges = list(map(int, input().split()))
    
    for i in range(len(edges)-1):
        a, b = edges[i], edges[i+1]
        indegree[b] += 1
        graph[a].append(b)

def topo_sort():
    result = []
    Q = deque([i for i in range(1, V+1) if indegree[i] == 0])
    while Q:
        i = Q.popleft()
        result.append(i)
        for j in graph[i]:
            indegree[j] -= 1
            if indegree[j] == 0:
                Q.append(j)
    return result

result = topo_sort()
if len(result) == V:
    print(*result, sep='\n')
else:
    print(0)