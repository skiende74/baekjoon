import sys
from collections import deque, defaultdict
from heapq import heappop, heappush

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [defaultdict(int) for _ in range(N+1)]

for _ in range(M):
    i, j, v = map(int, input().split())
    graph[i][j] = max(v, graph[i][j])
    graph[j][i] = max(v, graph[j][i])


INF = 1e9
max_val = [-1] * (N + 1)
def bfs(start, end):
    
    pq = []
    heappush(pq, (-INF, start))
    max_val[start] = INF
    #Q = deque()
    #Q.append((start, INF))
    while pq:
        
        v_i, i = heappop(pq)
        v_i = -v_i
        if (max_val[i] > v_i):
            continue

        for j, v_ij in graph[i].items():
            if min(v_ij, max_val[i]) > max_val[j]:
                max_val[j] = min(v_ij, max_val[i])
                heappush(pq, (-max_val[j], j))

                
    return max_val[end]


i,j = map(int, input().split())
print(bfs(i, j))