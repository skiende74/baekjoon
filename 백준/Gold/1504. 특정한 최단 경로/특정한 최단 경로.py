from heapq import heappush,heappop
import sys

input = sys.stdin.readline

V, E = map(int,input().split())
graph = [[] for _ in range(V+1)]
for _ in range(E):
    i,j,w = map(int,input().split())
    graph[i].append((j,w))
    graph[j].append((i,w))

v1,v2 = map(int,input().split())

INF = 10**9
def dijkstra(graph, start):
    global dist
    dist = [INF]*(V+1)
    dist[start] = 0
    PQ = [(0, start)]
    while PQ:
        d, i = heappop(PQ)

        for j, w in graph[i]:
            if dist[j] > d+w:
                dist[j] = d+w
                heappush(PQ, (dist[j],j))

dijkstra(graph, 1)
ans1 = dist[v1]
ans2 = dist[v2]
dijkstra(graph, v1)
ans2 += dist[V] + dist[v2]
dijkstra(graph, v2)
ans1 += dist[v1] + dist[V]
print(min(ans1,ans2) if min(ans1,ans2) < INF else -1)