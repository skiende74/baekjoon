from heapq import heappop, heappush
V, E, end = map(int,input().split())
graph = [[] for _ in range(V+1)]
graph_r = [[] for _ in range(V+1)]
for _ in range(E):
    i,j,w = map(int,input().split())
    graph[j].append((i,w))
    graph_r[i].append((j,w))

def dijkstra(dist, graph):
    PQ = [(0, end)]
    while PQ:
        d, i = heappop(PQ)
        if dist[i] < d: continue

        for j,w in graph[i]:
            if dist[j] > d+w:
                dist[j] = d+w
                heappush(PQ, (dist[j], j))


INF = 10**9
dist1 = [INF]*(V+1)
dist1[end] = 0
dist2 = dist1.copy()
dijkstra(dist1, graph)
dijkstra(dist2, graph_r)
dist = [ dist1[i]+dist2[i] for i in range(V+1)]
print(max(dist[1:]))