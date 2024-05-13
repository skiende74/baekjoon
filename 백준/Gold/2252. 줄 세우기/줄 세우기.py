import sys
from collections import deque

input = sys.stdin.readline

V, E = map(int,input().split())
indegree = [0]*(V+1)
graph = [[] for _ in range(V+1)]
for _ in range(E):
    i, j = map(int,input().split())
    graph[i].append(j)
    indegree[j] += 1


Q = deque([i for i in range(1,V+1) if indegree[i]==0])

result = []
while Q:
    i = Q.popleft()
    result.append(i)
    

    for j in graph[i]:
        indegree[j] -= 1
        
        if indegree[j] == 0:
            Q.append(j)
print(*result)