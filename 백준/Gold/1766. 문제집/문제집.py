import sys
from heapq import heappush, heappop

input = sys.stdin.readline
V, E = map(int,input().split())

graph = [[] for _ in range(V+1)]
indegree = [0]*(V+1)
for _ in range(E):
    i, j = map(int,input().split())
    graph[i].append(j)
    indegree[j] += 1
    
PQ = [ i for i in range(1,V+1) if indegree[i] == 0 ]

result = []
while PQ:
    i = heappop(PQ)
    result.append(i)
    for j in graph[i]:
        indegree[j] -= 1        
        if indegree[j] == 0:
            heappush(PQ, j)

print(*result)