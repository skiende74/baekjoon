from collections import deque
import sys
input = sys.stdin.readline
N = int(input())

graph = [[] for _ in range(N+1)]
times = [0]*(N+1)
start_times = [0]*(N+1)
indegree = [0]*(N+1)
for i in range(1, N+1):
    t, n, *prevs = map(int,input().split())
    times[i] = t
    indegree[i] = n
    for p in prevs:
        graph[p].append(i)

def bfs_topo():
    result = []
    Q = deque([i for i in range(1, N+1) if indegree[i]==0])
    while Q:
        i = Q.popleft()
        result.append(i)
        times[i] += start_times[i]
        for j in graph[i]:
            indegree[j] -=1
            start_times[j] = max(start_times[j], times[i])
            if indegree[j] == 0:
                Q.append(j)
    return result
bfs_topo()
print(max(times))