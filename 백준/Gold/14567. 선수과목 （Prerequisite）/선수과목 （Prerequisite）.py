import sys
input = sys.stdin.readline
from collections import deque
N, M = map(int,input().split())
edges = [list(map(int,input().split())) for _ in range(M)]

graph = [[] for _ in range(N+1)]
indegree = [0]*(N+1)
for i, j in edges:
    graph[i].append(j)
    indegree[j] += 1
    
def topo_sort():
    result = [0]*(N+1)
    Q = deque([(i, 1) for i in range(1, N+1) if indegree[i]==0])
    while Q:
        (i,cnt) = Q.popleft()
        # result.append((i,cnt))
        result[i] = cnt
        for j in graph[i]:
            indegree[j] -= 1
            if indegree[j] == 0: Q.append((j, cnt+1))
    return result

print(*topo_sort()[1:])