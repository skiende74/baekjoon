from heapq import heappop, heappush
import sys
input = sys.stdin.readline
V = int(input())
E = int(input())
graph = [[] for _ in range(V+1)]
for _ in range(E):
    i,j,w = map(int,input().split())
    graph[i].append((j,w))

S, E = map(int,input().split())

INF = 10**9
dist = [INF]*(V+1)
dist[S] = 0
PQ = [(0, S)]
while PQ:
    d, i = heappop(PQ)

    if d > dist[i]: continue

    for j,w in graph[i]:
        if dist[j] > dist[i]+w:
            dist[j] = dist[i]+w
            heappush(PQ, (dist[j], j))
print(dist[E])